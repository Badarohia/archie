"""Startup banner."""

from rich.console import Console

from archie.app.metadata import (
    APP_DESCRIPTION,
    APP_NAME,
    APP_VERSION,
)

console = Console()


def show_banner() -> None:
    """Display the Archie startup banner."""

    console.rule(f"[bold cyan]{APP_NAME}[/bold cyan]")

    console.print(f"[green]{APP_DESCRIPTION}[/green]")

    console.print(f"Version: [yellow]{APP_VERSION}[/yellow]\n")
