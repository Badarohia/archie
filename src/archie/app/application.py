"""Archie application."""

from __future__ import annotations

from dataclasses import dataclass

from archie.app.runtime import Runtime
from archie.app.service_manager import ServiceManager


@dataclass(slots=True)
class Archie:
    """The Archie application."""

    runtime: Runtime
    services: ServiceManager

    async def initialize(self) -> None:
        """Initialize Archie."""

        await self.services.initialize()

    async def start(self) -> None:
        """Start Archie."""

        await self.runtime.start()
        await self.services.start()

    async def stop(self) -> None:
        """Stop Archie."""

        await self.services.stop()
        await self.runtime.stop()
