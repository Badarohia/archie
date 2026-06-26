"""Service manager."""

from __future__ import annotations

from archie.services import BaseService
from archie.services.exceptions import DuplicateServiceError


class ServiceManager:
    """Manages Archie services."""

    def __init__(self) -> None:
        self._services: dict[str, BaseService] = {}

    def register(self, service: BaseService) -> None:
        """Register a service."""

        if service.name in self._services:
            raise DuplicateServiceError(f"Service '{service.name}' already registered.")

        self._services[service.name] = service

    async def initialize(self) -> None:
        """Initialize every registered service."""

        for service in self._services.values():
            await service.initialize()

    async def start(self) -> None:
        """Start every registered service."""

        for service in self._services.values():
            await service.start()

    async def stop(self) -> None:
        """Stop every registered service."""

        for service in reversed(tuple(self._services.values())):
            await service.stop()
