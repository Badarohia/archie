"""Chat message models."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from archie.models import ArchieModel


class ChatMessage(ArchieModel):
    """A single message in a conversation."""

    role: Literal[
        "system",
        "user",
        "assistant",
    ]

    content: str = Field(
        min_length=1,
    )
