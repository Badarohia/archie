"""Configuration manager."""

from __future__ import annotations

from pathlib import Path

import yaml
from pydantic import ValidationError

from archie.config.exceptions import (
    ConfigurationFileNotFoundError,
    ConfigurationValidationError,
)
from archie.config.models import Configuration


class ConfigurationManager:
    """Load and validate Archie configuration."""

    _config_directory: Path

    def __init__(self, config_directory: Path) -> None:
        self._config_directory = config_directory

    @property
    def config_directory(self) -> Path:
        return self._config_directory

    def load(self) -> Configuration:
        data = self._load_yaml("config.yaml")

        try:
            return Configuration.model_validate(data)
        except ValidationError as error:
            raise ConfigurationValidationError("Configuration validation failed.") from error

    def _load_yaml(self, filename: str) -> object:
        file_path = self._config_directory / filename

        if not file_path.exists():
            raise ConfigurationFileNotFoundError(f"Configuration file not found: {file_path}")

        try:
            with file_path.open("r", encoding="utf-8") as file:
                return yaml.safe_load(file)

        except yaml.YAMLError as error:
            raise ConfigurationValidationError(f"Failed to parse '{filename}'.") from error
