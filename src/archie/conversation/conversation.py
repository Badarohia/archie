"""Conversation model."""

from __future__ import annotations

from archie.brain import ChatMessage


class Conversation:
    """Represents an active conversation."""

    _messages: list[ChatMessage]

    def __init__(
        self,
        system_prompt: str,
    ) -> None:
        self._messages = [
            ChatMessage(
                role="system",
                content=system_prompt,
            )
        ]

    @property
    def messages(self) -> tuple[ChatMessage, ...]:
        """Return the conversation history."""

        return tuple(self._messages)

    def add_user_message(
        self,
        content: str,
    ) -> None:
        """Append a user message."""

        self._messages.append(
            ChatMessage(
                role="user",
                content=content,
            )
        )

    def add_assistant_message(
        self,
        content: str,
    ) -> None:
        """Append an assistant message."""

        self._messages.append(
            ChatMessage(
                role="assistant",
                content=content,
            )
        )

    def clear(self) -> None:
        """Reset the conversation while preserving the system prompt."""

        system_message = self._messages[0]
        self._messages = [system_message]