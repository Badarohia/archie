"""Application bootstrap."""

from __future__ import annotations

from archie.app.application import Archie
from archie.app.banner import show_banner
from archie.app.console import console
from archie.app.runtime import Runtime
from archie.app.service_manager import ServiceManager


async def bootstrap() -> Archie:
    """Create and initialize the Archie application."""

    show_banner()

    runtime = Runtime()
    services = ServiceManager()

    app = Archie(
        runtime=runtime,
        services=services,
    )
    console.print("[cyan]Bootstrapping Archie...[/cyan]")

    await app.initialize()

    return app
