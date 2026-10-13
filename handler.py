import logging
from typing import Any, Callable, Optional, TypeVar, Union

T = TypeVar('T')

logger = logging.getLogger(__name__)

class ExecutionError(Exception):
    """Base exception for utility operations."""

def safe_execute(func: Callable[..., T], *args: Any, **kwargs: Any) -> Optional[T]:
    """Execute function with robust error handling for edge cases."""
    try:
        if not callable(func):
            raise TypeError(f"Expected callable, got {type(func).__name__}")
        return func(*args, **kwargs)
    except (ValueError, TypeError, AttributeError, KeyError) as e:
        logger.error("Operational error in %s: %s", func.__name__, e)
    except Exception as e:
        logger.critical("Unexpected failure in %s: %s", func.__name__, e)
    return None

def validate_input(data: Any, expected_type: type) -> bool:
    """Validate input structure and type consistency."""
    if data is None:
        return False
    try:
        return isinstance(data, expected_type)
    except Exception:
        return False