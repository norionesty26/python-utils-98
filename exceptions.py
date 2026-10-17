from typing import Any, Optional


class UtilsBaseError(Exception):
    """Base exception for all python-utils-98 errors."""

    def __init__(self, message: str, details: Optional[dict[str, Any]] = None):
        super().__init__(message)
        self.message = message
        self.details = details or {}

    def __str__(self) -> str:
        if self.details:
            details_str = ", ".join(f"{k}={v}" for k, v in self.details.items())
            return f"{self.message} ({details_str})"
        return self.message


class ValidationError(UtilsBaseError):
    """Raised when data validation fails."""


class ConfigurationError(UtilsBaseError):
    """Raised when configuration loading or parsing fails."""


class ProcessingError(UtilsBaseError):
    """Raised when a processing operation fails."""


class ResourceNotFoundError(UtilsBaseError):
    """Raised when a requested resource is missing."""


def raise_for_condition(
    condition: bool,
    exception_cls: type[UtilsBaseError],
    message: str,
    **details: Any,
) -> None:
    if condition:
        raise exception_cls(message, details=details if details else None)


def format_exception_chain(exc: BaseException) -> str:
    chain = []
    current: Optional[BaseException] = exc
    while current:
        chain.append(f"{type(current).__name__}: {current}")
        current = current.__cause__ or current.__context__
    return " -> ".join(chain)
