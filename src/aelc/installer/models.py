"""Models for AELC installation."""

from enum import Enum

class Harness(str, Enum):
    """Supported AI coding harnesses."""

    CLAUDE = "claude"
    CODEX = "codex"
    
class HarnessSelection(str, Enum):
    """Supported harness installation options."""

    CLAUDE = "claude"
    CODEX = "codex"
    ALL = "all"

def get_selected_harnesses(selection: HarnessSelection) -> tuple[Harness, ...]:
    """Resolve the selected harnesses."""

    if selection == HarnessSelection.ALL:
        return tuple(Harness)

    return (Harness(selection.value),)
