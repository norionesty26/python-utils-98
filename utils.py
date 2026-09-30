import logging
from typing import Any, Callable, Optional

logger = logging.getLogger(__name__)

def safe_execute(func: Callable, *args: Any, default: Any = None, **kwargs: Any) -> Any:
    """Execute function with robust error handling for edge cases."""
    if not callable(func):
        raise ValueError(f"provided argument {func} is not callable")

    try:
        return func(*args, **kwargs)
    except (TypeError, ValueError, AttributeError) as e:
        logger.error(f"invalid input or operation in {func.__name__}: {e}")
        return default
    except Exception as e:
        logger.critical(f"unexpected system error in {func.__name__}: {e}", exc_info=True)
        return default

def validate_collection(data: Any, expected_type: type) -> bool:
    """Validate collection type and content presence."""
    if not isinstance(data, expected_type):
        return False
    if not data:
        return False
    return True

def get_nested_key(data: dict, keys: list, default: Any = None) -> Any:
    """Safely retrieve nested dictionary keys."""
    if not isinstance(data, dict):
        return default
    
    current = data
    try:
        for key in keys:
            current = current[key]
        return current
    except (KeyError, TypeError, IndexError):
        return default