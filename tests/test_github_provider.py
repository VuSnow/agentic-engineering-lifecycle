"""Tests for the AELC GitHub identity provider."""

import json
from io import BytesIO
from urllib.error import URLError
import pytest
from aelc.identity.models import ProviderIdentity
from aelc.identity.providers.base import AuthenticationError
from aelc.identity.providers.github import (
    DeviceCode,
    GitHubIdentityProvider,
    GITHUB_DEVICE_CODE_URL,
    GITHUB_ACCESS_TOKEN_URL,
    GITHUB_USER_API_URL,
)

DEVICE_RESPONSE = {
    "device_code": "fake-private-device-code",
    "user_code": "ABCD-1234",
    "verification_uri": "https://github.com/login/device",
    "expires_in": 900,
    "interval": 5,
}

TOKEN_RESPONSE = {
    "access_token": "fake-access-token",
    "token_type": "bearer",
}

USER_RESPONSE = {
    "id": 12345678,
    "login": "test-engineer",
}

class FakeClock:
    """Simulate elapsed time without real sleeping."""

    def __init__(self):
        self.current_time = 0.0
        self.sleep_calls = []

    def monotonic(self):
        return self.current_time

    def sleep(self, seconds):
        self.sleep_calls.append(seconds)
        self.current_time += seconds

class FakeGitHubProvider(GitHubIdentityProvider):
    """GitHub provider with simulated API responses."""

    def __init__(
        self,
        responses,
        *,
        clock=None,
        display=None,
    ):
        self.clock = clock or FakeClock()
        self.responses = list(responses)
        self.requests = []

        super().__init__(
            client_id="test-client-id",
            display=display or (lambda message: None),
            sleep=self.clock.sleep,
            monotonic=self.clock.monotonic,
        )

    def _request_json(
        self,
        url,
        *,
        payload=None,
        token=None,
    ):
        self.requests.append(
            {
                "url": url,
                "payload": payload,
                "token": token,
            }
        )

        return self.responses.pop(0)

def test_github_provider_name():
    provider = FakeGitHubProvider([])

    assert provider.name == "github"

def test_request_device_code():
    provider = FakeGitHubProvider(
        [DEVICE_RESPONSE]
    )

    device = provider._request_device_code()

    assert isinstance(device, DeviceCode)

    assert device.user_code == "ABCD-1234"
    assert device.expires_in == 900
    assert device.interval == 5

    assert provider.requests[0]["url"] == (
        GITHUB_DEVICE_CODE_URL
    )

    assert provider.requests[0]["payload"] == {
        "client_id": "test-client-id",
    }

def test_github_authentication_success():
    messages = []

    provider = FakeGitHubProvider(
        [
            DEVICE_RESPONSE,
            TOKEN_RESPONSE,
            USER_RESPONSE,
        ],
        display=messages.append,
    )

    identity = provider.authenticate()

    assert isinstance(identity, ProviderIdentity)

    assert identity.provider == "github"
    assert identity.subject == "12345678"
    assert identity.display_name == "test-engineer"
    assert identity.verification == "verified"

    assert provider.requests[1]["url"] == (
        GITHUB_ACCESS_TOKEN_URL
    )

    assert provider.requests[2]["url"] == (
        GITHUB_USER_API_URL
    )

    assert provider.requests[2]["token"] == (
        "fake-access-token"
    )

    assert any(
        "ABCD-1234" in message
        for message in messages
    )

    assert all(
        "fake-access-token" not in message
        for message in messages
    )

    assert provider.clock.sleep_calls == [5]

def test_authorization_pending():
    provider = FakeGitHubProvider(
        [
            DEVICE_RESPONSE,
            {"error": "authorization_pending"},
            TOKEN_RESPONSE,
            USER_RESPONSE,
        ]
    )

    identity = provider.authenticate()

    assert identity.subject == "12345678"

    assert provider.clock.sleep_calls == [
        5,
        5,
    ]

def test_polling_slow_down():
    provider = FakeGitHubProvider(
        [
            DEVICE_RESPONSE,
            {
                "error": "slow_down",
                "interval": 12,
            },
            TOKEN_RESPONSE,
            USER_RESPONSE,
        ]
    )

    identity = provider.authenticate()

    assert identity.verification == "verified"

    assert provider.clock.sleep_calls == [
        5,
        12,
    ]

def test_authorization_denied():
    provider = FakeGitHubProvider(
        [
            DEVICE_RESPONSE,
            {"error": "access_denied"},
        ]
    )

    with pytest.raises(
        AuthenticationError,
        match="denied",
    ):
        provider.authenticate()

def test_device_code_expired():
    expired_device = {
        **DEVICE_RESPONSE,
        "expires_in": 5,
    }

    provider = FakeGitHubProvider(
        [expired_device]
    )

    with pytest.raises(
        AuthenticationError,
        match="expired",
    ):
        provider.authenticate()

    assert len(provider.requests) == 1

def test_reject_invalid_github_user_id():
    provider = FakeGitHubProvider(
        [
            DEVICE_RESPONSE,
            TOKEN_RESPONSE,
            {
                "id": None,
                "login": "test-engineer",
            },
        ]
    )

    with pytest.raises(
        AuthenticationError,
        match="invalid user ID",
    ):
        provider.authenticate()

def test_reject_unexpected_verification_url():
    provider = FakeGitHubProvider(
        [
            {
                **DEVICE_RESPONSE,
                "verification_uri": (
                    "https://example.com/login"
                ),
            }
        ]
    )

    with pytest.raises(
        AuthenticationError,
        match="unexpected verification URL",
    ):
        provider.authenticate()

    assert len(provider.requests) == 1

def test_authenticated_user_request(monkeypatch):
    captured = {}

    def fake_urlopen(request, timeout):
        captured["url"] = request.full_url

        captured["authorization"] = request.get_header(
            "Authorization"
        )

        captured["timeout"] = timeout

        return BytesIO(
            json.dumps(USER_RESPONSE).encode("utf-8")
        )

    monkeypatch.setattr(
        "aelc.identity.providers.github.urlopen",
        fake_urlopen,
    )

    provider = GitHubIdentityProvider(
        client_id="test-client-id",
    )

    identity = provider._get_user_identity(
        "fake-access-token"
    )

    assert captured["url"] == GITHUB_USER_API_URL

    assert captured["authorization"] == (
        "Bearer fake-access-token"
    )

    assert captured["timeout"] == 120

    assert identity.subject == "12345678"

def test_github_network_error(monkeypatch):
    def fake_urlopen(request, timeout):
        raise URLError("Network unavailable")

    monkeypatch.setattr(
        "aelc.identity.providers.github.urlopen",
        fake_urlopen,
    )

    provider = GitHubIdentityProvider(
        client_id="test-client-id",
    )

    with pytest.raises(
        AuthenticationError,
        match="GitHub request failed",
    ):
        provider._request_device_code()
