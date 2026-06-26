"""Service related exceptions."""


class ServiceError(Exception):
    """Base exception for service errors."""


class DuplicateServiceError(ServiceError):
    """Raised when attempting to register a duplicate service."""
