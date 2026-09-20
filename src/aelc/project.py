
"""Project initialization and diagnostics."""

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path

from aelc import __version__


AELC_DIRECTORY = ".aelc"
PROJECT_CONFIG = "project.toml"
MANIFEST_FILE = "manifest.json"
SCHEMA_VERSION = 1


class ProjectError(Exception):
    """Raised when a project operation cannot be completed."""


@dataclass(frozen=True)
class ProjectStatus:
    """Result of inspecting an AELC project."""

    root: Path
    initialized: bool
    healthy: bool
    messages: tuple[str, ...]


def sha256(content: bytes) -> str:
    """Calculate a SHA-256 checksum."""

    return hashlib.sha256(content).hexdigest()


def resolve_project_root(path: Path) -> Path:
    """Resolve and validate an existing project directory."""

    root = path.expanduser().resolve()

    if not root.exists():
        raise ProjectError(
            f"Directory does not exist: {root}"
        )

    if not root.is_dir():
        raise ProjectError(
            f"Not a directory: {root}"
        )

    return root


def get_aelc_directory(root: Path) -> Path:
    """Return the framework state directory."""

    return root / AELC_DIRECTORY


def build_project_config(root: Path) -> bytes:
    """Generate the initial project configuration."""

    # JSON string quoting is compatible with TOML basic strings
    # for the project names generated here.
    project_name = json.dumps(root.name, ensure_ascii=True)

    content = (
        f"schema_version = {SCHEMA_VERSION}\n"
        f"name = {project_name}\n"
    )

    return content.encode("utf-8")


def build_manifest(config_content: bytes) -> bytes:
    """Generate a manifest for files managed by AELC."""

    manifest = {
        "schema_version": SCHEMA_VERSION,
        "framework_version": __version__,
        "managed_files": {
            f"{AELC_DIRECTORY}/{PROJECT_CONFIG}": {
                "sha256": sha256(config_content),
            }
        },
    }

    return (
        json.dumps(
            manifest,
            indent=2,
            ensure_ascii=False,
        )
        + "\n"
    ).encode("utf-8")


def inspect_project(path: Path) -> ProjectStatus:
    """Inspect project initialization and managed files."""

    root = resolve_project_root(path)
    aelc_dir = get_aelc_directory(root)

    if not aelc_dir.exists():
        return ProjectStatus(
            root=root,
            initialized=False,
            healthy=False,
            messages=("AELC has not been initialized.",),
        )

    if not aelc_dir.is_dir():
        return ProjectStatus(
            root=root,
            initialized=False,
            healthy=False,
            messages=(".aelc exists but is not a directory.",),
        )

    manifest_path = aelc_dir / MANIFEST_FILE

    if not manifest_path.is_file():
        return ProjectStatus(
            root=root,
            initialized=False,
            healthy=False,
            messages=("AELC manifest is missing.",),
        )

    try:
        manifest = json.loads(
            manifest_path.read_text(encoding="utf-8")
        )
    except (OSError, UnicodeError, json.JSONDecodeError):
        return ProjectStatus(
            root=root,
            initialized=False,
            healthy=False,
            messages=("AELC manifest cannot be read.",),
        )

    if not isinstance(manifest, dict):
        return ProjectStatus(
            root=root,
            initialized=False,
            healthy=False,
            messages=("Invalid manifest format.",),
        )

    if manifest.get("schema_version") != SCHEMA_VERSION:
        return ProjectStatus(
            root=root,
            initialized=True,
            healthy=False,
            messages=("Unsupported manifest schema version.",),
        )

    managed_files = manifest.get("managed_files")

    if not isinstance(managed_files, dict):
        return ProjectStatus(
            root=root,
            initialized=True,
            healthy=False,
            messages=("Invalid managed file manifest.",),
        )

    config_relative_path = (
        f"{AELC_DIRECTORY}/{PROJECT_CONFIG}"
    )

    # Foundation supports a fixed set of managed files.
    # Never trust arbitrary file paths from the manifest.
    if set(managed_files) != {config_relative_path}:
        return ProjectStatus(
            root=root,
            initialized=True,
            healthy=False,
            messages=("Unexpected managed file entries.",),
        )

    entry = managed_files[config_relative_path]

    if not isinstance(entry, dict):
        return ProjectStatus(
            root=root,
            initialized=True,
            healthy=False,
            messages=("Invalid project configuration entry.",),
        )

    expected_hash = entry.get("sha256")

    if not isinstance(expected_hash, str):
        return ProjectStatus(
            root=root,
            initialized=True,
            healthy=False,
            messages=("Invalid project configuration checksum.",),
        )

    config_path = aelc_dir / PROJECT_CONFIG

    if not config_path.is_file():
        return ProjectStatus(
            root=root,
            initialized=True,
            healthy=False,
            messages=("Project configuration is missing.",),
        )

    try:
        actual_hash = sha256(config_path.read_bytes())
    except OSError:
        return ProjectStatus(
            root=root,
            initialized=True,
            healthy=False,
            messages=("Project configuration cannot be read.",),
        )

    if actual_hash != expected_hash:
        return ProjectStatus(
            root=root,
            initialized=True,
            healthy=False,
            messages=("Project configuration has been modified.",),
        )

    return ProjectStatus(
        root=root,
        initialized=True,
        healthy=True,
        messages=("AELC project is healthy.",),
    )


def initialize_project(path: Path) -> ProjectStatus:
    """Initialize AELC without overwriting existing project data."""

    root = resolve_project_root(path)
    aelc_dir = get_aelc_directory(root)

    if aelc_dir.exists() or aelc_dir.is_symlink():
        status = inspect_project(root)

        if status.healthy:
            return status

        raise ProjectError(
            "Existing .aelc directory requires attention: "
            + "; ".join(status.messages)
        )

    config_content = build_project_config(root)
    manifest_content = build_manifest(config_content)

    try:
        # Do not silently reuse an existing directory.
        aelc_dir.mkdir(exist_ok=False)

        config_path = aelc_dir / PROJECT_CONFIG
        manifest_path = aelc_dir / MANIFEST_FILE

        # Exclusive creation prevents overwriting existing files.
        with config_path.open("xb") as file:
            file.write(config_content)

        with manifest_path.open("xb") as file:
            file.write(manifest_content)

    except OSError as exc:
        raise ProjectError(
            f"Cannot initialize AELC: {exc}"
        ) from exc

    return inspect_project(root)
