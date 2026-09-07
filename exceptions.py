class UtilityError(Exception):
    """Base exception for python-utils-98."""

class ConfigurationError(UtilityError):
    """Raised when configuration validation fails."""

class ProcessingError(UtilityError):
    """Raised during data transformation failures."""

class ValidationError(UtilityError):
    """Raised when input validation fails."""

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, TypeError, KeyError) as e:
            raise UtilityError(f"Operation failed: {e}") from e
    return wrapper

def validate_input(data, schema):
    if data is None:
        raise ValidationError("Input data cannot be None")
    if not isinstance(data, dict):
        raise ValidationError("Input data must be a dictionary")
    for key in schema:
        if key not in data:
            raise ValidationError(f"Missing required key: {key}")
    return True