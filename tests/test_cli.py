
"""Tests for AELC Foundation CLI."""

import json

from typer.testing import CliRunner

from aelc.cli import app
from aelc.project import (
    ProjectError,
    initialize_project,
    inspect_project,
)


runner = CliRunner()


def test_version():
    """CLI should display the framework version."""

    result = runner.invoke(app, ["--version"])

    assert result.exit_code == 0
    assert "AELC 0.1.0" in result.output


def test_init_creates_project_files(tmp_path):
    """Initializing a project should create managed files."""

    result = runner.invoke(
        app,
        ["init", "--path", str(tmp_path)],
    )

    assert result.exit_code == 0

    aelc_dir = tmp_path / ".aelc"

    assert aelc_dir.is_dir()
    assert (aelc_dir / "project.toml").is_file()
    assert (aelc_dir / "manifest.json").is_file()


def test_init_is_idempotent(tmp_path):
    """Repeated initialization must not modify managed files."""

    initialize_project(tmp_path)

    config_path = tmp_path / ".aelc" / "project.toml"
    manifest_path = tmp_path / ".aelc" / "manifest.json"

    original_config = config_path.read_bytes()
    original_manifest = manifest_path.read_bytes()

    result = runner.invoke(
        app,
        ["init", "--path", str(tmp_path)],
    )

    assert result.exit_code == 0
    assert config_path.read_bytes() == original_config
    assert manifest_path.read_bytes() == original_manifest


def test_doctor_detects_uninitialized_project(tmp_path):
    """Doctor should report missing AELC initialization."""

    result = runner.invoke(
        app,
        ["doctor", "--path", str(tmp_path)],
    )

    assert result.exit_code == 1
    assert "not been initialized" in result.output


def test_doctor_accepts_healthy_project(tmp_path):
    """Doctor should accept a valid initialized project."""

    initialize_project(tmp_path)

    result = runner.invoke(
        app,
        ["doctor", "--path", str(tmp_path)],
    )

    assert result.exit_code == 0
    assert "healthy" in result.output


def test_doctor_detects_modified_file(tmp_path):
    """Doctor should detect changes to a managed file."""

    initialize_project(tmp_path)

    config_path = tmp_path / ".aelc" / "project.toml"

    config_path.write_text(
        'schema_version = 1\nname = "modified"\n',
        encoding="utf-8",
    )

    result = runner.invoke(
        app,
        ["doctor", "--path", str(tmp_path)],
    )

    assert result.exit_code == 1
    assert "modified" in result.output


def test_init_does_not_overwrite_modified_file(tmp_path):
    """Initialization must preserve existing user changes."""

    initialize_project(tmp_path)

    config_path = tmp_path / ".aelc" / "project.toml"

    modified_content = (
        'schema_version = 1\n'
        'name = "my-custom-project"\n'
    )

    config_path.write_text(
        modified_content,
        encoding="utf-8",
    )

    result = runner.invoke(
        app,
        ["init", "--path", str(tmp_path)],
    )

    assert result.exit_code == 1

    assert (
        config_path.read_text(encoding="utf-8")
        == modified_content
    )


def test_manifest_contains_config_checksum(tmp_path):
    """Manifest should track the generated configuration."""

    initialize_project(tmp_path)

    manifest_path = tmp_path / ".aelc" / "manifest.json"

    manifest = json.loads(
        manifest_path.read_text(encoding="utf-8")
    )

    assert manifest["schema_version"] == 1

    assert (
        ".aelc/project.toml"
        in manifest["managed_files"]
    )


def test_init_rejects_nonexistent_directory(tmp_path):
    """Initialization should not create an arbitrary project root."""

    missing_path = tmp_path / "nonexistent"

    try:
        initialize_project(missing_path)
    except ProjectError:
        pass
    else:
        raise AssertionError(
            "Expected ProjectError for nonexistent directory"
        )

    assert not missing_path.exists()


def test_inspect_reports_healthy_project(tmp_path):
    """Project inspection should return structured status."""

    initialize_project(tmp_path)

    status = inspect_project(tmp_path)

    assert status.initialized is True
    assert status.healthy is True
    assert status.root == tmp_path.resolve()
