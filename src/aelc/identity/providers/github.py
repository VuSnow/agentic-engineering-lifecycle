"""GitHub OAuth Device Flow identity provider for AELC."""

import json
import time
from dataclasses import dataclass
from typing import Callable
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from aelc.identity.models import ProviderIdentity
from aelc.identity.providers.base import (
    AuthenticationError,
    IdentityProvider,
)

GITHUB_DEVICE_CODE_URL = (
    "https://github.com/login/device/code"
)

GITHUB_ACCESS_TOKEN_URL = (
    "https://github.com/login/oauth/access_token"
)

GITHUB_VERIFICATION_URL = (
    "https://github.com/login/device"
)

GITHUB_USER_API_URL = (
    "https://api.github.com/user"
)

DEVICE_GRANT_TYPE = (
    "urn:ietf:params:oauth:grant-type:device_code"
)

HTTP_TIMEOUT = 120

@dataclass(frozen=True)
class DeviceCode:
    """Represent a GitHub device authorization request."""

    device_code: str
    user_code: str
    verification_uri: str
    expires_in: int
    interval: int
    
def _require_text(value: object, field_name: str) -> str:
    """Require a non-empty string in a GitHub response."""

    if not isinstance(value, str) or not value.strip():
        raise AuthenticationError(
            f"GitHub response has an invalid {field_name}."
        )

    return value

class GitHubIdentityProvider(IdentityProvider):
    """Authenticate human engineers using GitHub OAuth."""

    def __init__(
        self,
        client_id: str,
        *,
        display: Callable[[str], None] = print,
        sleep: Callable[[float], None] = time.sleep,
        monotonic: Callable[[], float] = time.monotonic,
    ) -> None:
        """Initialize the GitHub identity provider."""

        if not isinstance(client_id, str) or not client_id.strip():
            raise ValueError(
                "GitHub OAuth Client ID cannot be empty."
            )

        self.client_id = client_id.strip()

        self._display = display
        self._sleep = sleep
        self._monotonic = monotonic

    @property
    def name(self) -> str:
        """Return the provider name."""

        return "github"
    
    def _request_json(
        self,
        url: str,
        *,
        payload: dict[str, str] | None = None,
        token: str | None = None,
    ) -> dict:
        """Send a GitHub API request and return JSON data."""

        headers = {
            "Accept": "application/json",
            "User-Agent": "AELC-CLI",
        }

        body = None
        method = "GET"

        if payload is not None:
            body = urlencode(payload).encode("utf-8")
            method = "POST"

            headers["Content-Type"] = (
                "application/x-www-form-urlencoded"
            )

        if token is not None:
            headers["Authorization"] = f"Bearer {token}"

        request = Request(
            url=url,
            data=body,
            headers=headers,
            method=method,
        )

        try:
            with urlopen(
                request,
                timeout=HTTP_TIMEOUT,
            ) as response:
                data = json.loads(
                    response.read().decode("utf-8")
                )

        except (
            HTTPError,
            URLError,
            TimeoutError,
            OSError,
            ValueError,
            UnicodeError,
        ) as exc:
            raise AuthenticationError(
                "GitHub request failed or returned invalid JSON."
            ) from exc

        if not isinstance(data, dict):
            raise AuthenticationError(
                "GitHub returned an invalid JSON response."
            )

        return data

    def _request_device_code(self) -> DeviceCode:
        """Request a new device authorization code."""

        response = self._request_json(
            GITHUB_DEVICE_CODE_URL,
            payload={
                "client_id": self.client_id,
            },
        )

        device_code = _require_text(
            response.get("device_code"),
            "device_code",
        )

        user_code = _require_text(
            response.get("user_code"),
            "user_code",
        )

        verification_uri = _require_text(
            response.get("verification_uri"),
            "verification_uri",
        )

        if verification_uri != GITHUB_VERIFICATION_URL:
            raise AuthenticationError(
                "GitHub returned an unexpected verification URL."
            )

        expires_in = response.get("expires_in")
        interval = response.get("interval", 5)

        if type(expires_in) is not int or expires_in <= 0:
            raise AuthenticationError(
                "GitHub returned an invalid expiration time."
            )

        if type(interval) is not int or interval <= 0:
            raise AuthenticationError(
                "GitHub returned an invalid polling interval."
            )

        return DeviceCode(
            device_code=device_code,
            user_code=user_code,
            verification_uri=verification_uri,
            expires_in=expires_in,
            interval=max(5, interval),
        )

    def _poll_for_token(
        self,
        device: DeviceCode,
    ) -> str:
        """Poll GitHub until authorization succeeds or expires."""

        deadline = self._monotonic() + device.expires_in
        interval = max(5, device.interval)

        while True:
            remaining = deadline - self._monotonic()

            if remaining <= 0:
                raise AuthenticationError(
                    "GitHub device authorization expired."
                )

            # Respect GitHub's minimum polling interval.
            self._sleep(min(interval, remaining))

            if self._monotonic() >= deadline:
                raise AuthenticationError(
                    "GitHub device authorization expired."
                )

            response = self._request_json(
                GITHUB_ACCESS_TOKEN_URL,
                payload={
                    "client_id": self.client_id,
                    "device_code": device.device_code,
                    "grant_type": DEVICE_GRANT_TYPE,
                },
            )

            error = response.get("error")

            if error == "authorization_pending":
                continue

            if error == "slow_down":
                new_interval = response.get("interval")

                interval += 5

                if (
                    type(new_interval) is int
                    and new_interval > interval
                ):
                    interval = new_interval

                continue

            if error == "access_denied":
                raise AuthenticationError(
                    "GitHub authorization was denied."
                )

            if error in ("expired_token", "token_expired"):
                raise AuthenticationError(
                    "GitHub device authorization expired."
                )

            if error is not None:
                raise AuthenticationError(
                    "GitHub device authorization failed."
                )

            token = _require_text(
                response.get("access_token"),
                "access_token",
            )

            token_type = _require_text(
                response.get("token_type"),
                "token_type",
            )

            if token_type.lower() != "bearer":
                raise AuthenticationError(
                    "GitHub returned an unsupported token type."
                )

            return token

    def _get_user_identity(
        self,
        token: str,
    ) -> ProviderIdentity:
        """Resolve the authenticated GitHub user's identity."""

        response = self._request_json(
            GITHUB_USER_API_URL,
            token=token,
        )

        github_id = response.get("id")

        if (
            type(github_id) is not int
            or github_id <= 0
        ):
            raise AuthenticationError(
                "GitHub returned an invalid user ID."
            )

        login = _require_text(
            response.get("login"),
            "login",
        )

        return ProviderIdentity(
            provider=self.name,
            subject=str(github_id),
            display_name=login,
            verification="verified",
        )

    def authenticate(self) -> ProviderIdentity:
        """Authenticate a human engineer through GitHub."""

        device = self._request_device_code()

        self._display(
            "Open the following URL to authorize AELC:"
        )

        self._display(device.verification_uri)

        self._display(
            f"Enter verification code: {device.user_code}"
        )

        token = self._poll_for_token(device)

        return self._get_user_identity(token)
