
"""Deploy AELC skills to supported AI coding harnesses."""

from dataclasses import dataclass
from importlib.resources import files
from pathlib import Path
from typing import Literal

from .models import HarnessSelection, get_selected_harnesses


SKILL_NAME = "aelc-init"
SKILL_FILENAME = "SKILL.md"

HARNESS_DIRECTORIES = {
    "claude": ".claude",
    "codex": ".agents",
}

@dataclass(frozen=True)
class AdapterInstallResult:
    """Represent the result of installing one harness adapter."""

    harness: str
    destination: Path
    status: Literal["installed", "unchanged"]

def get_harness_home(
    harness: str,
    home: Path | None = None,
) -> Path:
    """Return the user-level directory for a harness."""

    directory = HARNESS_DIRECTORIES.get(harness)

    if directory is None:
        raise ValueError(
            f"Unsupported harness: {harness}"
        )

    user_home = Path.home() if home is None else home

    return user_home / directory

def get_skill_destination(
    harness: str,
    home: Path | None = None,
) -> Path:
    """Return the destination of the AELC init skill."""

    harness_home = get_harness_home(
        harness=harness,
        home=home,
    )

    return (
        harness_home
        / "skills"
        / SKILL_NAME
        / SKILL_FILENAME
    )

def load_skill_content() -> str:
    """Load the shared AELC init skill from package resources."""

    skill_resource = (
        files("aelc")
        .joinpath("resources", SKILL_NAME, SKILL_FILENAME)
    )

    return skill_resource.read_text(encoding="utf-8")

def validate_skill_destination(
    destination: Path,
    content: str,
) -> Literal["install", "unchanged"]:
    """Check whether a skill can be installed safely."""

    skill_directory = destination.parent

    if skill_directory.is_symlink():
        raise FileExistsError(
            f"Skill directory is a symbolic link: "
            f"{skill_directory}"
        )

    if destination.is_symlink():
        raise FileExistsError(
            f"Skill file is a symbolic link: {destination}"
        )

    if destination.exists():
        if not destination.is_file():
            raise FileExistsError(
                f"Skill destination is not a file: "
                f"{destination}"
            )

        existing_content = destination.read_text(
            encoding="utf-8"
        )

        if existing_content == content:
            return "unchanged"

        raise FileExistsError(
            f"Skill already exists with different content: "
            f"{destination}"
        )

    if skill_directory.exists():
        if not skill_directory.is_dir():
            raise FileExistsError(
                f"Skill destination is not a directory: "
                f"{skill_directory}"
            )

        if any(skill_directory.iterdir()):
            raise FileExistsError(
                f"Skill directory contains existing files: "
                f"{skill_directory}"
            )

    return "install"

def install_harness_adapters(
    selection: HarnessSelection,
    home: Path | None = None,
) -> list[AdapterInstallResult]:
    """Install the AELC init skill for selected harnesses."""

    harnesses = get_selected_harnesses(selection)
    content = load_skill_content()

    installation_plan = []

    # Validate every destination before writing files.
    for harness in harnesses:
        harness_name = getattr(harness, "value", harness)

        destination = get_skill_destination(
            harness=harness_name,
            home=home,
        )

        action = validate_skill_destination(
            destination=destination,
            content=content,
        )

        installation_plan.append(
            (harness_name, destination, action)
        )

    results = []

    # Apply the validated installation plan.
    for harness_name, destination, action in installation_plan:

        if action == "unchanged":
            results.append(
                AdapterInstallResult(
                    harness=harness_name,
                    destination=destination,
                    status="unchanged",
                )
            )
            continue

        destination.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        # Exclusive creation prevents overwriting a file
        # that may have appeared after validation.
        with destination.open(
            mode="x",
            encoding="utf-8",
            newline="\n",
        ) as skill_file:
            skill_file.write(content)

        results.append(
            AdapterInstallResult(
                harness=harness_name,
                destination=destination,
                status="installed",
            )
        )

    return results