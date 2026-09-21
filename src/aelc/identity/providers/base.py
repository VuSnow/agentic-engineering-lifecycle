
"""Base interface for AELC identity providers."""

from abc import ABC, abstractmethod
from aelc.identity.models import ProviderIdentity

class IdentityProviderError(Exception):
    """Base exception for identity provider failures."""

class AuthenticationError(IdentityProviderError):
    """Raised when identity authentication fails."""

class IdentityProvider(ABC):
    """Abstract interface for external identity providers."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the unique provider name."""

    @abstractmethod
    def authenticate(self) -> ProviderIdentity:
        """Authenticate a user and return their provider identity."""
