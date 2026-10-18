"""Custom exception hierarchy for utility operations."""

from typing import Any, Optional


class BaseUtilError(Exception):
    """Base exception for all python-utils-98 errors."""

    def __init__(self, message: str, details: Optional[Any] = None) -> None:
        super().__init__(message)
        self.message = message
        self.details = details

    def __str__(self) -> str:
        if self.details is not None:
            return f"{self.message} (details: {self.details})"
        return self.message


class ValidationError(BaseUtilError):
    """Raised when data validation fails."""

    def __init__(
        self, message: str, field: Optional[str] = None, details: Optional[Any] = None
    ) -> None:
        super().__init__(message, details)
        self.field = field

    def __str__(self) -> str:
        base_msg = super().__str__()
        if self.field:
            return f"Validation failed for '{self.field}': {base_msg}"
        return base_msg


class ConfigurationError(BaseUtilError):
    """Raised when application configuration is invalid or missing."""


class ProcessingError(BaseUtilError):
    """Raised when an error occurs during utility processing."""


class TimeoutError(BaseUtilError):
    """Raised when a timed utility operation exceeds allowed duration."""

    def __init__(
        self, message: str, timeout: float, details: Optional[Any] = None
    ) -> None:
        super().__init__(message, details)
        self.timeout = timeout
