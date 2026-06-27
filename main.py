"""Application entry point."""

from __future__ import annotations

import asyncio

from rich.console import Console

from archie.app import bootstrap

console = Console()


async def main() -> None:
    """Run the Archie application."""

    app = bootstrap()

    try:
        await app.run()

    except KeyboardInterrupt:
        console.print("\n[yellow]Interrupted by user.[/yellow]")

    finally:
        console.print("[green]Goodbye.[/green]")


if __name__ == "__main__":
    asyncio.run(main())