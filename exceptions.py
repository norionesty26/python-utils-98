class BaseUtilsError(Exception):
    """Base exception for python-utils-98."""


class ConfigurationError(BaseUtilsError):
    """Raised for invalid library configurations."""


class ValidationError(BaseUtilsError):
    """Raised when data validation fails."""


class ProcessingError(BaseUtilsError):
    """Raised during core utility operations."""


class ResourceNotFoundError(BaseUtilsError):
    """Raised when a required resource is missing."""


class InitializationError(BaseUtilsError):
    """Raised when component initialization fails."""