import logging
from typing import Any, Callable, Optional

logger = logging.getLogger(__name__)

class ProcessingError(Exception):
    """Custom exception for handler operations."""
    pass

def safe_execute(func: Callable, *args: Any, **kwargs: Any) -> Optional[Any]:
    """Executes a callable with comprehensive error handling."""
    try:
        return func(*args, **kwargs)
    except TypeError as e:
        logger.error(f"Invalid argument type provided: {e}")
    except ValueError as e:
        logger.error(f"Invalid value encountered: {e}")
    except KeyError as e:
        logger.error(f"Missing required key: {e}")
    except Exception as e:
        logger.exception(f"Unexpected system failure: {e}")
    return None

def validate_input(data: Any) -> bool:
    """Validates input presence and structure."""
    if data is None:
        return False
    if isinstance(data, (dict, list, str)) and not data:
        return False
    return True

def process_with_validation(data: Any, processor: Callable) -> Any:
    """Wraps processing logic with safety checks."""
    if not validate_input(data):
        raise ProcessingError("Invalid input data received")
    
    result = safe_execute(processor, data)
    if result is None:
        raise ProcessingError("Processor execution failed")
    return result