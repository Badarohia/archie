"""Configuration exceptions."""


class ConfigurationError(Exception):
    """Base exception for configuration errors."""


class ConfigurationFileNotFoundError(ConfigurationError):
    """Raised when a configuration file is missing."""


class ConfigurationValidationError(ConfigurationError):
    """Raised when configuration validation fails."""
