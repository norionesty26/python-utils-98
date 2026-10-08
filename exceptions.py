class DataHandlingError(Exception):
    """Base exception for data operations."""

class ValidationError(DataHandlingError):
    """Raised when data fails schema validation."""

class ProcessingError(DataHandlingError):
    """Raised when data transformation fails."""

class ConfigurationError(DataHandlingError):
    """Raised when system configuration is invalid."""

def raise_if_none(data, label="data"):
    if data is None:
        raise ValidationError(f"Missing required field: {label}")
    return data

def validate_type(data, expected_type, label="data"):
    if not isinstance(data, expected_type):
        raise ValidationError(
            f"{label} must be {expected_type.__name__}, got {type(data).__name__}"
        )
    return data

def safe_execute(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        raise ProcessingError(f"Operation failed: {str(e)}") from e