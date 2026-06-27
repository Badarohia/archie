"""Brain interface."""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Sequence

from archie.brain.message import ChatMessage
from archie.brain.response import ChatResponse


class Brain(ABC):
    """Abstract interface for language models."""

    @abstractmethod
    def generate(
        self,
        messages: Sequence[ChatMessage],
    ) -> ChatResponse:
        """Generate the next assistant response."""