"""Tests for the AELC identity provider interface."""

import pytest
from aelc.identity.models import ProviderIdentity
from aelc.identity.providers.base import (
    IdentityProvider,
    AuthenticationError,
)

class FakeIdentityProvider(IdentityProvider):
    """Fake provider used for unit testing."""

    @property
    def name(self) -> str:
        return "fake"

    def authenticate(self) -> ProviderIdentity:
        return ProviderIdentity(
            provider=self.name,
            subject="fake-user-123",
            display_name="Test Engineer",
            verification="self_declared",
        )

def test_provider_name():
    provider = FakeIdentityProvider()

    assert provider.name == "fake"

def test_provider_authenticate():
    provider = FakeIdentityProvider()

    identity = provider.authenticate()

    assert isinstance(identity, ProviderIdentity)

    assert identity.provider == "fake"
    assert identity.subject == "fake-user-123"

def test_cannot_instantiate_abstract_provider():
    with pytest.raises(TypeError):
        IdentityProvider()

def test_authentication_error():
    with pytest.raises(AuthenticationError):
        raise AuthenticationError(
            "Authentication failed."
        )
