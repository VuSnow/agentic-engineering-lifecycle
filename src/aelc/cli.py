
"""AELC command-line interface."""

from pathlib import Path

import typer

from aelc import __version__
from aelc.project import (
    ProjectError,
    initialize_project,
    inspect_project,
)
from aelc.ui import print_welcome, print_status
from aelc.installer.models import HarnessSelection
from aelc.installer.service import InstallationError, prepare_installation
from .installer.models import HarnessSelection
from .installer.service import complete_installation
from .installer.prerequisites import PrerequisiteError


app = typer.Typer(
    name="aelc",
    help="Agentic Engineering Lifecycle CLI.",
    no_args_is_help=True,
)


def version_callback(value: bool) -> None:
    """Display the framework version."""

    if value:
        print_welcome("version")
        typer.echo(f"AELC {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        False,
        "--version",
        help="Show the installed AELC version.",
        callback=version_callback,
        is_eager=True,
    ),
) -> None:
    """AELC command-line entry point."""


@app.command()
def init(
    path: Path = typer.Option(
        Path("."),
        "--path",
        "-p",
        help="Directory of the project to initialize.",
    ),
) -> None:
    """Initialize AELC in a project."""
    print_welcome("init")
    print_status("Initializing AELC in your project...")
    
    try:
        status = initialize_project(path)
    except ProjectError as exc:
        typer.echo(f"Error: {exc}", err=True)
        raise typer.Exit(code=1) from exc
    typer.echo(f"AELC project: {status.root}")
    typer.echo("Initialization verified.")

@app.command()
def doctor(
    path: Path = typer.Option(
        Path("."),
        "--path",
        "-p",
        help="Directory of the project to inspect.",
    ),
) -> None:
    """Check the current AELC project."""
    
    print_welcome("doctor")

    try:
        status = inspect_project(path)

    except ProjectError as exc:
        typer.echo(f"Error: {exc}", err=True)
        raise typer.Exit(code=1) from exc

    typer.echo(f"Project: {status.root}")

    for message in status.messages:
        typer.echo(message)

    if not status.healthy:
        raise typer.Exit(code=1)
    
@app.command("install-check")
def install_check(
    harness: HarnessSelection = typer.Option(
        ...,
        "--harness",
        help="AI Coding harness to install AELC for."
    )
) -> None:
    """Validate prerequisites for global AELC installation."""
    
    print_welcome("installation")
    typer.echo("Checking installation prerequisites...")
    
    try:
        plan = prepare_installation(harness)
    except InstallationError as exc:
        typer.echo(
            f"Error: {exc}",
            err=True
        )
        raise typer.Exit(code=1) from exc
    
    for info in plan.harnesses:
        typer.echo(
            f"[OK] {info.harness.value}: "
            f"{info.executable_path}"
        )
        
    typer.echo(
        "All installation prerequisites satisfied."
    )

@app.command("install-harness")
def install_harness(
    harness: HarnessSelection = typer.Option(
        ...,
        "--harness",
        help="Target harness: claude, codex, or all."
    ),
) -> None:
    """Install AELC skills into selected AI coding harnesses."""

    typer.echo("Installing AELC harness adapters...")
    
    try:
        results = complete_installation(harness)
    except (PrerequisiteError, OSError, ValueError) as exc:
        typer.echo(
            f"Installation failed: {exc}",
            err=True
        )
        raise typer.Exit(code=1) from exc
    
    for result in results:
        typer.echo(
            f"[{result.status}] "
            f"{result.harness}: "
            f"{result.destination}"
        )
        
    typer.echo("Harness adapter installation completed.")