"""Application entry point."""

from __future__ import annotations

import asyncio

from rich.console import Console

from archie.app import bootstrap

console = Console()


async def main() -> None:
    """Run the Archie application."""

    app = await bootstrap()

    await app.start()

    console.print("[green]✓ Archie is online[/green]")
    console.print("Press Ctrl+C to exit.\n")

    try:
        while True:
            await asyncio.sleep(1)

    except KeyboardInterrupt:
        console.print("\n[yellow]Stopping Archie...[/yellow]")

    finally:
        await app.stop()

        console.print("[green]Goodbye.[/green]")


if __name__ == "__main__":
    asyncio.run(main())
