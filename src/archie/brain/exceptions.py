"""Brain exceptions."""


class BrainError(Exception):
    """Base exception for brain errors."""


class GenerationError(BrainError):
    """Raised when text generation fails."""
