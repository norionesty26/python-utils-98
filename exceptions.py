class BaseUtilsError(Exception):
    """Base exception for python-utils-98."""


class ConfigurationError(BaseUtilsError):
    """Raised when configuration is invalid."""


class ValidationError(BaseUtilsError):
    """Raised when data validation fails."""


class ProcessingError(BaseUtilsError):
    """Raised during internal processing stages."""


class ResourceNotFoundError(BaseUtilsError):
    """Raised when a requested resource is missing."""


class OperationTimeoutError(BaseUtilsError):
    """Raised when an operation exceeds duration limits."""