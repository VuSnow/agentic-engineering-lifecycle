
"""AELC installation service."""

from dataclasses import dataclass
from pathlib import Path

from aelc.installer.models import (
    Harness,
    HarnessSelection,
    get_selected_harnesses,
)
from aelc.installer.prerequisites import (
    PrerequisiteError,
    check_harness_prerequisite,
)

from .adapter import AdapterInstallResult, install_harness_adapters


@dataclass(frozen=True)
class HarnessInfo:
    """Information about an available AI coding harness."""

    harness: Harness
    executable_path: Path

@dataclass(frozen=True)
class InstallationPlan:
    """Validated installation plan."""

    harnesses: tuple[HarnessInfo, ...]

class InstallationError(Exception):
    """Raised when installation requirements are not satisfied."""

def prepare_installation(
    selection: HarnessSelection,
) -> InstallationPlan:
    """Validate all selected harnesses before installation."""

    selected_harnesses = get_selected_harnesses(selection)

    available: list[HarnessInfo] = []
    errors: list[str] = []

    for harness in selected_harnesses:
        try:
            executable_path = check_harness_prerequisite(
                harness
            )

        except PrerequisiteError as exc:
            errors.append(str(exc))
            continue

        available.append(
            HarnessInfo(
                harness=harness,
                executable_path=executable_path,
            )
        )

    if errors:
        raise InstallationError(
            "Installation prerequisites failed:\n\n"
            + "\n\n".join(errors)
        )

    return InstallationPlan(
        harnesses=tuple(available),
    )

def complete_installation(
    selection: HarnessSelection,
) -> list[AdapterInstallResult]:
    """Validate the environment and install harness adapters."""
    
    # Reuse the prerequisite validation from Step 2.
    prepare_installation(selection)

    # Deploy skills only after prerequisites are satisfied.
    return install_harness_adapters(selection)
