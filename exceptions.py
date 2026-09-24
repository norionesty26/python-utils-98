from typing import Optional, Any

class UtilsError(Exception):
    """Base exception for python-utils-98 package."""
    pass

class ConfigurationError(UtilsError):
    """Raised when configuration requirements are not met."""
    def __init__(self, message: str, key: Optional[str] = None) -> None:
        self.key = key
        super().__init__(f"{message}: {key}" if key else message)

class ValidationError(UtilsError):
    """Raised when input data fails validation criteria."""
    def __init__(self, message: str, value: Any = None) -> None:
        self.value = value
        super().__init__(message)

class ProcessingError(UtilsError):
    """Raised during failure of core logic execution."""
    def __init__(self, message: str, context: Optional[dict] = None) -> None:
        self.context = context or {}
        super().__init__(message)

def raise_if_none(value: Any, name: str) -> None:
    """Check if value is None and raise ValidationError."""
    if value is None:
        raise ValidationError(f"Missing required value: {name}")