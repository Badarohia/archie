"""Configuration models."""

from __future__ import annotations

from pathlib import Path

from archie.config.base import ConfigModel


class AppConfig(ConfigModel):
    """Application configuration."""

    name: str
    version: str
    debug: bool


class PathsConfig(ConfigModel):
    """Filesystem paths."""

    storage: Path
    cache: Path
    logs: Path


class LLMConfig(ConfigModel):
    """Language model configuration."""

    provider: str
    model: str
    host: str
    timeout: int


class Configuration(ConfigModel):
    """Root configuration."""

    app: AppConfig
    paths: PathsConfig
    llm: LLMConfig
