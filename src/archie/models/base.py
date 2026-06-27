"""Base Pydantic model for Archie."""

from __future__ import annotations

from typing import ClassVar

from pydantic import BaseModel, ConfigDict


class ArchieModel(BaseModel):
    """Base model for all Archie domain models."""

    model_config: ClassVar[ConfigDict] = ConfigDict(
        frozen=True,
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
    )