import logging
from typing import Any, Callable, Optional

logger = logging.getLogger(__name__)

class ProcessingError(Exception):
    """Custom exception for handler operations."""

def safe_execute(func: Callable, *args: Any, **kwargs: Any) -> Optional[Any]:
    """Executes a callable with comprehensive error handling."""
    if not callable(func):
        logger.error("Provided argument is not a callable object")
        return None

    try:
        return func(*args, **kwargs)
    except (ValueError, TypeError, KeyError) as e:
        logger.warning(f"Handled input-related exception: {e}")
    except PermissionError:
        logger.critical("Insufficient permissions to perform operation")
    except Exception as e:
        logger.exception(f"Unexpected error occurred: {type(e).__name__}")
        raise ProcessingError(f"Critical failure in {func.__name__}") from e
    
    return None

def validate_data(data: Any) -> bool:
    """Validates input data against edge cases."""
    try:
        if data is None:
            return False
        if isinstance(data, (list, dict, str)) and not data:
            return False
        return True
    except Exception:
        return False