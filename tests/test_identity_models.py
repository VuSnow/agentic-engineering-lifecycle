"""Tests for AELC identity domain models."""

import pytest

from aelc.identity.models import (
    HumanIdentity,
    ProviderIdentity,
)

def test_create_human_identity():
    identity = HumanIdentity(
        display_name="Engineer A"
    )

    assert identity.display_name == "Engineer A"
    assert identity.human_id

def test_human_id_is_unique():
    first = HumanIdentity(
        display_name="Engineer A"
    )

    second = HumanIdentity(
        display_name="Engineer B"
    )

    assert first.human_id != second.human_id

def test_restore_existing_human_identity():
    identity = HumanIdentity(
        display_name="Engineer A",
        human_id="existing-human-id",
    )

    assert identity.human_id == "existing-human-id"

def test_reject_empty_human_name():
    with pytest.raises(ValueError):
        HumanIdentity(
            display_name="  "
        )

def test_create_github_identity():
    identity = ProviderIdentity(
        provider="github",
        subject="12345678",
        display_name="Engineer A",
        verification="verified",
    )

    assert identity.provider == "github"
    assert identity.subject == "12345678"
    assert identity.verification == "verified"

def test_create_local_identity():
    identity = ProviderIdentity(
        provider="local",
        subject="local-user-id",
        display_name="Engineer A",
        verification="self_declared",
    )

    assert identity.provider == "local"
    assert identity.verification == "self_declared"

def test_reject_verified_local_identity():
    with pytest.raises(ValueError):
        ProviderIdentity(
            provider="local",
            subject="local-user-id",
            display_name="Engineer A",
            verification="verified",
        )

def test_reject_empty_provider_subject():
    with pytest.raises(ValueError):
        ProviderIdentity(
            provider="github",
            subject="",
            display_name="Engineer A",
            verification="verified",
        )