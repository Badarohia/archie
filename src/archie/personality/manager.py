"""Personality manager."""

from __future__ import annotations

from pathlib import Path


class PersonalityManager:
    """Loads the Archie system prompt."""

    _prompt: str

    def __init__(
        self,
        prompt_file: Path,
    ) -> None:
        self._prompt = prompt_file.read_text(
            encoding="utf-8",
        ).strip()

    @property
    def prompt(self) -> str:
        """Return the system prompt."""

        return self._prompt