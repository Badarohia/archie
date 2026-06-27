"""Archie application."""

from __future__ import annotations

from dataclasses import dataclass

from archie.app.repl import REPL
from archie.container.application import ApplicationContainer


@dataclass(slots=True)
class Archie:
    """The Archie application."""

    container: ApplicationContainer

    async def initialize(self) -> None:
        """Initialize Archie."""

        await self.container.services.initialize()

    async def start(self) -> None:
        """Start Archie."""

        await self.container.runtime.start()
        await self.container.services.start()

    async def stop(self) -> None:
        """Stop Archie."""

        await self.container.services.stop()
        await self.container.runtime.stop()

    async def run(self) -> None:
        """Run Archie."""

        await self.initialize()
        await self.start()

        try:
            repl = REPL(
                brain=self.container.brain,
                personality=self.container.personality,
            )

            await repl.run()

        finally:
            await self.stop()