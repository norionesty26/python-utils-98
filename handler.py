import logging
from typing import Any, Callable, Optional

logger = logging.getLogger(__name__)

class ProcessingError(Exception):
    """Base exception for data processing."""
    pass

def safe_execute(func: Callable, *args: Any, **kwargs: Any) -> Optional[Any]:
    """Executes a callable with comprehensive error handling."""
    if not callable(func):
        logger.error("Provided object is not callable")
        return None

    try:
        return func(*args, **kwargs)
    except (ValueError, TypeError) as err:
        logger.error(f"Invalid input data: {err}")
    except ConnectionError as err:
        logger.warning(f"Network connectivity failure: {err}")
    except Exception as err:
        logger.critical(f"Unexpected system failure: {err}", exc_info=True)
    return None

def validate_input(data: Any) -> bool:
    """Checks input integrity before processing."""
    try:
        if data is None:
            raise ValueError("Input data is null")
        if not isinstance(data, (dict, list, str)):
            raise TypeError("Unsupported data format")
        return True
    except (ValueError, TypeError) as err:
        logger.error(f"Validation failed: {err}")
        return False