import logging
from typing import Any, Callable, Optional

logger = logging.getLogger(__name__)

class ProcessingError(Exception):
    """Base exception for data processing operations."""

def safe_execute(func: Callable, *args: Any, **kwargs: Any) -> Optional[Any]:
    """Execute function with robust error handling for edge cases."""
    try:
        if not callable(func):
            raise ValueError("Provided object is not callable")
        return func(*args, **kwargs)
    except (TypeError, ValueError) as e:
        logger.error(f"Invalid input parameters: {e}")
    except (KeyboardInterrupt, SystemExit):
        raise
    except Exception as e:
        logger.critical(f"Unexpected system failure: {e}")
    return None

def validate_response(data: Any) -> bool:
    """Validate edge case response structures."""
    if data is None:
        return False
    if isinstance(data, (dict, list)) and not data:
        return False
    return True

def batch_process(items: list, processor: Callable) -> list:
    """Process collection with per-item fault tolerance."""
    results = []
    for item in items or []:
        try:
            results.append(processor(item))
        except Exception:
            continue
    return results