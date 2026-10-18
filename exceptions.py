class BaseUtilsError(Exception):
    """Base exception for the library."""


class ConfigurationError(BaseUtilsError):
    """Raised when configuration is invalid."""


class ValidationError(BaseUtilsError):
    """Raised when input validation fails."""


class ProcessingError(BaseUtilsError):
    """Raised during data processing failures."""


class ResourceNotFoundError(BaseUtilsError):
    """Raised when a requested resource is missing."""


class TimeoutError(BaseUtilsError):
    """Raised on operation timeout."""


class InitializationError(BaseUtilsError):
    """Raised when component fails to initialize."""


def handle_exception(exc: Exception) -> None:
    if not isinstance(exc, BaseUtilsError):
        raise BaseUtilsError(f"Unexpected error: {exc}") from exc
    raise exc