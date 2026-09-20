
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
