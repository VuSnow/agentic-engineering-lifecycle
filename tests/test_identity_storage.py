
"""Tests for AELC local identity storage."""

import json
import os
import pytest
from aelc.identity.models import HumanIdentity
from aelc.identity.storage import (
    IdentityStorage,
    IdentityStorageError,
    IdentityAlreadyExistsError,
    InvalidIdentityFileError,
)


def test_load_missing_identity(tmp_path):
    path = tmp_path / ".aelc" / "identity.json"

    storage = IdentityStorage(path=path)

    result = storage.load()

    assert result is None
    assert not path.exists()
    assert not path.parent.exists()

def test_save_identity(tmp_path):
    path = tmp_path / ".aelc" / "identity.json"

    storage = IdentityStorage(path=path)

    identity = HumanIdentity(
        display_name="Engineer A"
    )

    result = storage.save(identity)

    assert result == "created"
    assert path.is_file()

    data = json.loads(
        path.read_text(encoding="utf-8")
    )

    assert data["schema_version"] == 1
    assert data["human_id"] == identity.human_id
    assert data["display_name"] == "Engineer A"
    
def test_load_existing_identity(tmp_path):
    path = tmp_path / ".aelc" / "identity.json"

    storage = IdentityStorage(path=path)

    original = HumanIdentity(
        display_name="Engineer A"
    )

    storage.save(original)

    # Simulate starting AELC again.
    new_storage = IdentityStorage(path=path)

    restored = new_storage.load()

    assert restored is not None
    assert restored == original

    assert restored.human_id == original.human_id

def test_save_same_identity_twice(tmp_path):
    path = tmp_path / ".aelc" / "identity.json"

    storage = IdentityStorage(path=path)

    identity = HumanIdentity(
        display_name="Engineer A"
    )

    first_result = storage.save(identity)

    original_content = path.read_bytes()

    second_result = storage.save(identity)

    assert first_result == "created"
    assert second_result == "unchanged"

    assert path.read_bytes() == original_content

def test_reject_different_identity(tmp_path):
    path = tmp_path / ".aelc" / "identity.json"

    storage = IdentityStorage(path=path)

    first_identity = HumanIdentity(
        display_name="Engineer A"
    )

    second_identity = HumanIdentity(
        display_name="Engineer B"
    )

    storage.save(first_identity)

    with pytest.raises(IdentityAlreadyExistsError):
        storage.save(second_identity)

    restored = storage.load()

    assert restored == first_identity

def test_reject_corrupted_identity_file(tmp_path):
    path = tmp_path / ".aelc" / "identity.json"

    storage = IdentityStorage(path=path)

    identity = HumanIdentity(
        display_name="Engineer A"
    )

    storage.save(identity)

    path.write_text(
        "{invalid json",
        encoding="utf-8",
    )

    with pytest.raises(InvalidIdentityFileError):
        storage.load()
        

def test_reject_unsupported_schema(tmp_path):
    path = tmp_path / ".aelc" / "identity.json"

    storage = IdentityStorage(path=path)

    identity = HumanIdentity(
        display_name="Engineer A"
    )

    storage.save(identity)

    data = json.loads(
        path.read_text(encoding="utf-8")
    )

    data["schema_version"] = 999

    path.write_text(
        json.dumps(data),
        encoding="utf-8",
    )

    with pytest.raises(InvalidIdentityFileError):
        storage.load()


def test_reject_unexpected_fields(tmp_path):
    path = tmp_path / ".aelc" / "identity.json"

    storage = IdentityStorage(path=path)

    identity = HumanIdentity(
        display_name="Engineer A"
    )

    storage.save(identity)

    data = json.loads(
        path.read_text(encoding="utf-8")
    )

    data["access_token"] = "unexpected-secret"

    path.write_text(
        json.dumps(data),
        encoding="utf-8",
    )

    with pytest.raises(InvalidIdentityFileError):
        storage.load()
        

@pytest.mark.skipif(
    os.name == "nt",
    reason="POSIX symlink behavior test",
)
def test_reject_identity_symlink(tmp_path):
    path = tmp_path / ".aelc" / "identity.json"

    path.parent.mkdir(mode=0o700)

    target = tmp_path / "external-identity.json"

    target.write_text(
        "Existing external data",
        encoding="utf-8",
    )

    path.symlink_to(target)

    storage = IdentityStorage(path=path)

    with pytest.raises(IdentityStorageError):
        storage.save(
            HumanIdentity(
                display_name="Engineer A"
            )
        )

    assert target.read_text(
        encoding="utf-8"
    ) == "Existing external data"
    

