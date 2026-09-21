"""Tests for AELC harness adapter deployment."""

import pytest
from aelc.installer.adapter import (get_harness_home, get_skill_destination, load_skill_content, validate_skill_destination, install_harness_adapters)
from aelc.installer.models import HarnessSelection


def test_get_claude_home(tmp_path): 
    result = get_harness_home(
    harness="claude", home=tmp_path, )
    assert result == tmp_path / ".claude"


def test_get_codex_home(tmp_path): 
    result = get_harness_home(
    harness="codex", home=tmp_path, )
    assert result == tmp_path / ".agents"

def test_unsupported_harness(tmp_path): 
    with pytest.raises(ValueError): 
        get_harness_home(harness="unsupported", home=tmp_path)
        

def test_claude_skill_destination(tmp_path): 
    destination = get_skill_destination(harness="claude", home=tmp_path, )
    assert destination == (tmp_path / ".claude" / "skills" / "aelc-init" / "SKILL.md")


def test_codex_skill_destination(tmp_path): 
    destination = get_skill_destination(harness="codex", home=tmp_path, )
    assert destination == (tmp_path / ".agents" / "skills" / "aelc-init" / "SKILL.md" )
    

def test_load_skill_content(): 
    content = load_skill_content()
    assert "name: aelc-init" in content 
    assert "aelc init" in content 
    assert "aelc doctor" in content
    

def test_install_codex_adapter(tmp_path): 
    results = install_harness_adapters(selection=HarnessSelection.CODEX, home=tmp_path)
    destination = get_skill_destination(harness="codex", home=tmp_path)
    assert len(results) == 1
    assert results[0].harness == "codex"
    assert results[0].status == "installed"
    assert destination.is_file()
    assert destination.read_text(encoding="utf-8") == load_skill_content()
    
def test_repeated_installation(tmp_path):
    first_result = install_harness_adapters(selection=HarnessSelection.CODEX, home=tmp_path)
    second_result = install_harness_adapters(selection=HarnessSelection.CODEX, home=tmp_path)
    
    assert first_result[0].status == "installed"
    assert second_result[0].status == "unchanged"
    
def test_modified_skill_is_not_overwritten(tmp_path):
    install_harness_adapters(selection=HarnessSelection.CODEX, home=tmp_path)
    destination = get_skill_destination(harness="codex", home=tmp_path)
    custom_content = "# My custom skill"
    destination.write_text(custom_content, encoding="utf-8")
    
    with pytest.raises(FileExistsError):
        install_harness_adapters(selection=HarnessSelection.CODEX, home=tmp_path)
    
    assert destination.read_text(encoding="utf-8") == custom_content
    
def test_existing_skill_directory_is_preserved(tmp_path):
    destination = get_skill_destination(harness="codex", home=tmp_path)
    destination.parent.mkdir(parents=True)
    custom_file = destination.parent / "custom.txt"
    custom_file.write_text("Existing user data", encoding="utf-8")
    
    with pytest.raises(FileExistsError):
        install_harness_adapters(selection=HarnessSelection.CODEX, home=tmp_path)
    
    assert custom_file.read_text(encoding="utf-8") == "Existing user data"
    assert not destination.exists()
    
def test_install_all_adapters(tmp_path):
    results = install_harness_adapters(selection=HarnessSelection.ALL, home=tmp_path)
    assert len(results) == 2
    
    claude_destination = get_skill_destination(harness="claude", home=tmp_path)
    codex_destination = get_skill_destination(harness="codex", home=tmp_path)
    
    assert claude_destination.is_file()
    assert codex_destination.is_file()
    assert {result.status for result in results} == {"installed"}
    
def test_all_installation_validates_before_writing(tmp_path):
    codex_destination = get_skill_destination(harness="codex", home=tmp_path)
    codex_destination.parent.mkdir(parents=True)
    codex_destination.write_text("# Existing custom skill", encoding="utf-8")
    
    with pytest.raises(FileExistsError):
        install_harness_adapters(selection=HarnessSelection.ALL, home=tmp_path)
    
    claude_destionation = get_skill_destination(harness="claude", home=tmp_path)
    assert not claude_destionation.exists()
    assert codex_destination.read_text(encoding="utf-8") == "# Existing custom skill"
