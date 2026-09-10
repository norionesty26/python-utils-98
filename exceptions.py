from typing import Any, Optional


class UtilsError(Exception):
    """Base exception class for all library errors."""

    def __init__(self, message: str, details: Optional[Any] = None) -> None:
        super().__init__(message)
        self.message = message
        self.details = details


class ValidationError(UtilsError):
    """Raised when validation on input data fails."""


class ConfigurationError(UtilsError):
    """Raised when application configuration is invalid or missing."""


class ResourceNotFoundError(UtilsError):
    """Raised when a requested resource cannot be found."""


class ProcessExecutionError(UtilsError):
    """Raised when an external or internal process execution fails."""

    def __init__(
        self, message: str, return_code: Optional[int] = None, details: Optional[Any] = None
    ) -> None:
        super().__init__(message, details)
        self.return_code = return_code
