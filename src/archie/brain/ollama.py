"""Ollama brain implementation."""

from __future__ import annotations

from collections.abc import Sequence
from typing import override

import httpx

from archie.brain.base import Brain
from archie.brain.exceptions import GenerationError
from archie.brain.message import ChatMessage
from archie.brain.response import ChatResponse


class OllamaBrain(Brain):
    """Brain implementation backed by Ollama."""

    _client: httpx.Client
    _host: str
    _model: str

    def __init__(
        self,
        host: str,
        model: str,
        timeout: float = 120.0,
    ) -> None:
        """Initialize the Ollama client."""

        self._host = host.rstrip("/")
        self._model = model

        self._client = httpx.Client(
            base_url=self._host,
            timeout=timeout,
        )

    @override
    def generate(
        self,
        messages: Sequence[ChatMessage],
    ) -> ChatResponse:
        """Generate a response using Ollama."""

        payload = {
            "model": self._model,
            "messages": [
                {
                    "role": message.role,
                    "content": message.content,
                }
                for message in messages
            ],
            "stream": False,
        }

        try:
            response = self._client.post(
                "/api/chat",
                json=payload,
            )

            response = response.raise_for_status()

        except httpx.HTTPStatusError as error:
            raise GenerationError(
                f"Ollama returned HTTP {error.response.status_code}."
            ) from error
        
        except httpx.RequestError as error:
            raise GenerationError(
                "Could not connect to the Ollama server."
            ) from error

        data = response.json()

        try:
            message = data["message"]
            content = message["content"]

        except (KeyError, TypeError) as error:
            raise GenerationError(
                "Invalid response received from Ollama."
            ) from error

        return ChatResponse(
            content=str(content),
        )

    def close(self) -> None:
        """Close the HTTP client."""

        self._client.close()

    def __enter__(self) -> OllamaBrain:
        """Enter the context manager."""

        return self

    def __exit__(
        self,
        exc_type: object,
        exc_value: object,
        traceback: object,
    ) -> None:
        """Exit the context manager."""

        self.close()