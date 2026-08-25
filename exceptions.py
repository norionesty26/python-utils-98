import traceback
from typing import Any, Callable, Dict, Optional, Type

class UtilsError(Exception):
    pass

class ValidationError(UtilsError):
    def __init__(self, message: str, field: Optional[str] = None) -> None:
        super().__init__(message)
        self.field = field

class ConfigurationError(UtilsError):
    pass

class ProcessingError(UtilsError):
    pass

def raise_if_not(condition: bool, exception_cls: Type[UtilsError], message: str) -> None:
    if not condition:
        raise exception_cls(message)

def raise_if_none(value: Any, exception_cls: Type[UtilsError], message: str) -> None:
    if value is None:
        raise exception_cls(message)

def get_exception_details(exc: Exception) -> Dict[str, Any]:
    return {
        "type": type(exc).__name__,
        "message": str(exc),
        "args": exc.args,
        "traceback": traceback.format_exc()
    }

def safe_execute(func: Callable[..., Any], *args: Any, **kwargs: Any) -> Optional[Any]:
    try:
        return func(*args, **kwargs)
    except Exception:
        return None

def execute_with_default(func: Callable[..., Any], default: Any, *args: Any, **kwargs: Any) -> Any:
    try:
        return func(*args, **kwargs)
    except Exception:
        return default

def format_error(exc: Exception) -> str:
    return f"{exc.__class__.__name__}: {str(exc)}"

def chain_exceptions(original: Exception, new_exception: Exception) -> None:
    raise new_exception from original