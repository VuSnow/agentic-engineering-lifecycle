"""Domain models for AELC human identity."""

from dataclasses import dataclass, field
from typing import Literal
from uuid import uuid4

VerificationLevel = Literal[
    "verified",
    "self_declared",
]

@dataclass(frozen=True)
class HumanIdentity:
    """Represent a human engineer within AELC."""

    display_name: str
    human_id: str = field(
        default_factory=lambda: str(uuid4())
    )

    def __post_init__(self) -> None:
        """Validate the human identity."""

        if not self.human_id.strip():
            raise ValueError(
                "Human ID cannot be empty."
            )

        if not self.display_name.strip():
            raise ValueError(
                "Display name cannot be empty."
            )

@dataclass(frozen=True)
class ProviderIdentity:
    """Represent an identity returned by an identity provider."""

    provider: str
    subject: str
    display_name: str
    verification: VerificationLevel

    def __post_init__(self) -> None:
        """Validate the provider identity."""

        if not self.provider.strip():
            raise ValueError(
                "Identity provider cannot be empty."
            )

        if not self.subject.strip():
            raise ValueError(
                "Provider subject cannot be empty."
            )

        if not self.display_name.strip():
            raise ValueError(
                "Display name cannot be empty."
            )

        if self.verification not in (
            "verified",
            "self_declared",
        ):
            raise ValueError(
                "Invalid verification level."
            )

        if (
            self.provider == "local"
            and self.verification == "verified"
        ):
            raise ValueError(
                "Local identity cannot be marked as verified."
            )
