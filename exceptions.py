from typing import Any, Dict, Optional


class BaseUtilsError(Exception):
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(message)
        self.message = message
        self.details = details or {}

    def to_dict(self) -> Dict[str, Any]:
        return {
            "error_type": self.__class__.__name__,
            "message": self.message,
            "details": self.details,
        }


class ValidationError(BaseUtilsError):
    def __init__(self, message: str, field: Optional[str] = None, **kwargs: Any):
        details = kwargs.get("details", {})
        if field:
            details["field"] = field
        super().__init__(message, details=details)


class ConfigurationError(BaseUtilsError):
    pass


class ProcessingError(BaseUtilsError):
    pass


class ResourceNotFoundError(BaseUtilsError):
    def __init__(self, resource_type: str, resource_id: Any):
        message = f"{resource_type} '{resource_id}' was not found"
        super().__init__(message, details={"type": resource_type, "id": resource_id})


class TimeoutError(BaseUtilsError):
    pass
