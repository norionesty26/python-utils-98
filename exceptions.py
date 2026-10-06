class UtilsError(Exception):
    """Base exception for python-utils-98"""

class ConfigurationError(UtilsError):
    """Raised when configuration is invalid"""

class ValidationError(UtilsError):
    """Raised when data validation fails"""

class ProcessingError(UtilsError):
    """Raised when data processing fails"""

def handle_exception(exc: Exception) -> None:
    if isinstance(exc, UtilsError):
        print(f"Utils Error: {exc}")
    else:
        print(f"Unexpected Error: {exc}")

class ExceptionContext:
    def __init__(self, exception_type: type):
        self.exception_type = exception_type

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None and issubclass(exc_type, self.exception_type):
            return True
        return False