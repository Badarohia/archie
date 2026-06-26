"""Base configuration model."""

from __future__ import annotations

from typing import ClassVar

from pydantic import BaseModel, ConfigDict


class ConfigModel(BaseModel):
    """Base class for all Archie configuration models."""

    model_config: ClassVar[ConfigDict] = ConfigDict(
        frozen=True,
        extra="forbid",
    )
