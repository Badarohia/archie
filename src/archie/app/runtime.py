"""Runtime state for the Archie application."""

from enum import Enum, auto


class RuntimeState(Enum):
    """Possible runtime states."""

    STOPPED = auto()
    STARTING = auto()
    RUNNING = auto()
    STOPPING = auto()


class Runtime:
    """Tracks the current lifecycle state of the application."""

    def __init__(self) -> None:
        self._state: RuntimeState = RuntimeState.STOPPED

    @property
    def state(self) -> RuntimeState:
        """Return the current runtime state."""
        return self._state

    async def start(self) -> None:
        """Transition to the running state."""
        self._state = RuntimeState.RUNNING

    async def stop(self) -> None:
        """Transition to the stopped state."""
        self._state = RuntimeState.STOPPED
