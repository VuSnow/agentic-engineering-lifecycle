"""Tests for the AELC installer."""

import shutil

import pytest

from aelc.installer.models import (
    Harness,
    HarnessSelection,
    get_selected_harnesses,
)
from aelc.installer.prerequisites import (
    PrerequisiteError,
    check_harness_prerequisite,
    get_harness_executable,
    is_harness_installed,
)
from aelc.installer.service import (
    InstallationError,
    prepare_installation,
)

# =========================================
# Harness selection
# =========================================


def test_select_claude():
    result = get_selected_harnesses(
        HarnessSelection.CLAUDE
    )

    assert result == (Harness.CLAUDE,)


def test_select_codex():
    result = get_selected_harnesses(
        HarnessSelection.CODEX
    )

    assert result == (Harness.CODEX,)


def test_select_all():
    result = get_selected_harnesses(
        HarnessSelection.ALL
    )

    assert result == (
        Harness.CLAUDE,
        Harness.CODEX,
    )

# =========================================
# Executable mapping
# =========================================


def test_claude_executable():
    assert get_harness_executable(
        Harness.CLAUDE
    ) == "claude"


def test_codex_executable():
    assert get_harness_executable(
        Harness.CODEX
    ) == "codex"


# =========================================
# Prerequisite checks
# =========================================
def test_harness_is_installed(monkeypatch):

    monkeypatch.setattr(
        shutil,
        "which",
        lambda command: "/usr/local/bin/claude",
    )

    assert is_harness_installed(
        Harness.CLAUDE
    ) is True


def test_harness_is_not_installed(monkeypatch):

    monkeypatch.setattr(
        shutil,
        "which",
        lambda command: None,
    )

    assert is_harness_installed(
        Harness.CLAUDE
    ) is False


def test_missing_harness_raises_error(monkeypatch):

    monkeypatch.setattr(
        shutil,
        "which",
        lambda command: None,
    )

    with pytest.raises(PrerequisiteError):
        check_harness_prerequisite(
            Harness.CLAUDE
        )


# =========================================
# Installation service
# =========================================
def test_prepare_claude_installation(monkeypatch):

    monkeypatch.setattr(
        shutil,
        "which",
        lambda command: "/usr/local/bin/claude",
    )

    plan = prepare_installation(
        HarnessSelection.CLAUDE
    )

    assert len(plan.harnesses) == 1

    assert (
        plan.harnesses[0].harness
        == Harness.CLAUDE
    )


def test_prepare_all_installation(monkeypatch):

    def fake_which(command: str) -> str | None:
        return f"/usr/local/bin/{command}"

    monkeypatch.setattr(
        shutil,
        "which",
        fake_which,
    )

    plan = prepare_installation(
        HarnessSelection.ALL
    )

    assert len(plan.harnesses) == 2

    assert {
        info.harness for info in plan.harnesses
    } == {
        Harness.CLAUDE,
        Harness.CODEX,
    }


def test_prepare_all_fails_if_codex_missing(monkeypatch):

    def fake_which(command: str) -> str | None:

        if command == "claude":
            return "/usr/local/bin/claude"

        return None

    monkeypatch.setattr(
        shutil,
        "which",
        fake_which,
    )

    with pytest.raises(InstallationError):
        prepare_installation(
            HarnessSelection.ALL
        )
