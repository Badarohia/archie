"""Base class for all Archie services."""

from __future__ import annotations

from enum import Enum, auto


class ServiceState(Enum):
    """Lifecycle state of a service."""

    CREATED = auto()
    INITIALIZED = auto()
    RUNNING = auto()
    STOPPED = auto()


class BaseService:
    """Base class for all Archie services."""

    def __init__(self, name: str) -> None:
        self._name: str = name
        self._state: ServiceState = ServiceState.CREATED

    @property
    def name(self) -> str:
        """Return the service name."""
        return self._name

    @property
    def state(self) -> ServiceState:
        """Return the current service state."""
        return self._state

    async def initialize(self) -> None:
        """Initialize the service."""
        self._state = ServiceState.INITIALIZED

    async def start(self) -> None:
        """Start the service."""
        self._state = ServiceState.RUNNING

    async def stop(self) -> None:
        """Stop the service."""
        self._state = ServiceState.STOPPED
