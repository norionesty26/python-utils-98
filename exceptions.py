class BaseUtilsError(Exception):
    """Base exception for python-utils-98."""

class ConfigurationError(BaseUtilsError):
    """Raised when configuration is invalid."""

class ValidationError(BaseUtilsError):
    """Raised when data validation fails."""

class ExecutionError(BaseUtilsError):
    """Raised when a process execution fails."""

def handle_error(e: Exception, logger=None) -> None:
    """Centralized exception processing."""
    if logger:
        logger.error(f"{e.__class__.__name__}: {str(e)}")
    raise e

class ExceptionContext:
    """Context manager for error suppression."""
    def __init__(self, exception_type=Exception, suppress=False):
        self.exception_type = exception_type
        self.suppress = suppress

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type and issubclass(exc_type, self.exception_type):
            return self.suppress
        return False