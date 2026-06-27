"""Logging manager."""

from __future__ import annotations

import logging
import logging.config
from pathlib import Path

import yaml


class LoggingManager:
    """Configure the application's logging."""

    _config_file: Path

    def __init__(self, config_file: Path) -> None:
        self._config_file = config_file

    def configure(self) -> None:
        """Configure Python logging."""

        with self._config_file.open(
            "r",
            encoding="utf-8",
        ) as file:
            config = yaml.safe_load(file)

        logging.config.dictConfig(config)
