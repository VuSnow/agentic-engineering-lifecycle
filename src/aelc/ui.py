
"""Terminal UI components for AELC."""
from pyfiglet import Figlet
from rich import box
from rich.align import Align
from rich.console import Console, Group
from rich.panel import Panel
from rich.text import Text

console = Console()

def print_welcome(command: str | None = None) -> None:
    """Display the AELC welcome banner."""

    figlet = Figlet(font="ansi_shadow", width=200, justify="left")
    
    ascii_art = figlet.renderText("DATA-GLHF.exe")
    ascii_art = ascii_art.rstrip("\n")
    
    # Team branding.
    team_name = Text(
        ascii_art,
        style="bold #C4B5FD",
        no_wrap=True,
        overflow="ignore"
    )

    # Framework name.
    framework_name = Text(
        "AELC - Agentic Engineering Lifecycle",
        style="bold white",
        justify="center",
    )

    # framework_description = Text(
    #     "Agentic Engineering Lifecycle",
    #     style="#A1A1AA",
    #     justify="center",
    # )

    # Copyright information.
    copyright_text = Text(
        "© 2026 DATA-GLHF.exe. All rights reserved.",
        style="#A1A1AA",
        justify="center",
    )

    # Combine branding components.
    content = Group(
        # Text(""),
        team_name,
        # Text(""),
        framework_name,
        # framework_description,
        # Text(""),
        copyright_text,
        # Text(""),
    )

    # Dynamic panel title.
    title = "AELC"

    if command:
        title = f"AELC — {command}"

    # Render the welcome screen.
    console.print(
        Panel(
            Align.center(content),
            title=title,
            title_align="left",
            border_style="#454545",
            box=box.ROUNDED,
            padding=(1, 3),
            expand=True,
        )
    )


def print_status(message: str) -> None:
    """Display a command status message."""

    console.print(
        Text(
            message,
            style="#86EFAC",
        )
    )
