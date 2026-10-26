class BaseUtilsError(Exception):
    """Base exception for python-utils-98."""


class ConfigurationError(BaseUtilsError):
    """Raised when configuration parameters are invalid."""


class ValidationError(BaseUtilsError):
    """Raised when input validation fails."""


class ProcessingError(BaseUtilsError):
    """Raised during internal data transformation steps."""


class ResourceNotFoundError(BaseUtilsError):
    """Raised when a required resource is missing."""


class InitializationError(BaseUtilsError):
    """Raised during component startup failures."""