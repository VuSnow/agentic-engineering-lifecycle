
"""Local storage for AELC human identity."""

import json
import os
import stat
from pathlib import Path
from typing import Literal
from aelc.identity.models import HumanIdentity


SCHEMA_VERSION = 1

class IdentityStorageError(Exception):
    """Base exception for identity storage failures."""

class IdentityAlreadyExistsError(IdentityStorageError):
    """Raised when a different identity already exists."""

class InvalidIdentityFileError(IdentityStorageError):
    """Raised when stored identity data is invalid."""

class IdentityStorage:
    """Store the current human identity on the local machine."""

    def __init__(
        self,
        path: Path | None = None,
    ) -> None:
        """Initialize the identity storage location."""

        self.path = (
            Path.home() / ".aelc" / "identity.json"
            if path is None
            else Path(path)
        )
        
    def _check_directory(self) -> None:
        """Validate the identity storage directory."""

        directory = self.path.parent

        if directory.is_symlink():
            raise IdentityStorageError(
                f"Identity directory cannot be a symlink: "
                f"{directory}"
            )

        if not directory.exists():
            return

        if not directory.is_dir():
            raise IdentityStorageError(
                f"Identity storage path is not a directory: "
                f"{directory}"
            )

        if os.name != "nt":
            permissions = stat.S_IMODE(
                directory.stat().st_mode
            )

            if permissions & 0o077:
                raise IdentityStorageError(
                    f"Identity directory has unsafe permissions: "
                    f"{directory}. Expected mode 0700."
                )
                
    def load(self) -> HumanIdentity | None:
        """Load the current human identity from local storage."""

        self._check_directory()

        if self.path.is_symlink():
            raise IdentityStorageError(
                f"Identity file cannot be a symlink: "
                f"{self.path}"
            )

        if not self.path.exists():
            return None

        if not self.path.is_file():
            raise IdentityStorageError(
                f"Identity storage path is not a file: "
                f"{self.path}"
            )

        if os.name != "nt":
            permissions = stat.S_IMODE(
                self.path.stat().st_mode
            )

            if permissions & 0o077:
                raise IdentityStorageError(
                    f"Identity file has unsafe permissions: "
                    f"{self.path}. Expected mode 0600."
                )

        try:
            content = self.path.read_text(
                encoding="utf-8"
            )

            data = json.loads(content)

        except (json.JSONDecodeError, UnicodeError) as exc:
            raise InvalidIdentityFileError(
                f"Cannot decode identity file: {self.path}"
            ) from exc

        if not isinstance(data, dict):
            raise InvalidIdentityFileError(
                "Identity file must contain a JSON object."
            )

        required_fields = {
            "schema_version",
            "human_id",
            "display_name",
        }

        if set(data) != required_fields:
            raise InvalidIdentityFileError(
                "Identity file contains missing or "
                "unexpected fields."
            )

        if (
            type(data["schema_version"]) is not int
            or data["schema_version"] != SCHEMA_VERSION
        ):
            raise InvalidIdentityFileError(
                "Unsupported identity schema version."
            )

        if not isinstance(data["human_id"], str):
            raise InvalidIdentityFileError(
                "Human ID must be a string."
            )

        if not isinstance(data["display_name"], str):
            raise InvalidIdentityFileError(
                "Display name must be a string."
            )

        try:
            return HumanIdentity(
                human_id=data["human_id"],
                display_name=data["display_name"],
            )

        except ValueError as exc:
            raise InvalidIdentityFileError(
                "Stored human identity is invalid."
            ) from exc
            
    def save(
        self,
        identity: HumanIdentity,
    ) -> Literal["created", "unchanged"]:
        """Save a human identity without overwriting existing data."""

        existing_identity = self.load()

        if existing_identity is not None:
            if existing_identity == identity:
                return "unchanged"

            raise IdentityAlreadyExistsError(
                "A different human identity already exists. "
                "Explicit identity switching is required."
            )

        self.path.parent.mkdir(
            mode=0o700,
            parents=True,
            exist_ok=True,
        )

        self._check_directory()

        data = {
            "schema_version": SCHEMA_VERSION,
            "human_id": identity.human_id,
            "display_name": identity.display_name,
        }

        content = json.dumps(
            data,
            indent=2,
            ensure_ascii=False,
        ) + "\n"

        flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL

        if hasattr(os, "O_NOFOLLOW"):
            flags |= os.O_NOFOLLOW

        try:
            file_descriptor = os.open(
                self.path,
                flags,
                0o600,
            )

        except FileExistsError as exc:
            raise IdentityAlreadyExistsError(
                "Identity file already exists. "
                "Refusing to overwrite it."
            ) from exc

        with os.fdopen(
            file_descriptor,
            mode="w",
            encoding="utf-8",
            newline="\n",
        ) as identity_file:
            identity_file.write(content)

        return "created"
