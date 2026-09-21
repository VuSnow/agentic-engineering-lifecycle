
"""Installation prerequisite checks."""

import shutil
from pathlib import Path

from aelc.installer.models import Harness


class PrerequisiteError(Exception):
    """Raised when an installation prerequisite is missing."""


def get_harness_executable(harness: Harness) -> str:
    """Return the executable name for a harness."""

    executables = {
        Harness.CLAUDE: "claude",
        Harness.CODEX: "codex",
    }

    try:
        return executables[harness]
    except KeyError as exc:
        raise PrerequisiteError(f"Unsupported harness: {harness}") from exc

def get_harness_path(harness: Harness) -> Path | None:
    """Find the selected harness executable."""

    executable = get_harness_executable(harness)

    path = shutil.which(executable)

    if path is None:
        return None

    return Path(path)

def is_harness_installed(harness: Harness) -> bool:
    """Check whether the harness executable is available."""
    return get_harness_path(harness) is not None

def check_harness_prerequisite(harness: Harness) -> Path:
    """Validate that the selected harness is available."""

    path = get_harness_path(harness)

    if path is None:
        executable = get_harness_executable(harness)

        raise PrerequisiteError(
            f"Harness '{harness.value}' was not found.\n"
            f"Expected executable: {executable}\n"
            "Please install the selected harness "
            "and ensure it is available in PATH."
        )

    return path
