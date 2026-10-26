import logging
from typing import Any, Callable, Optional

logger = logging.getLogger(__name__)

class ProcessingError(Exception):
    pass

def safe_execute(func: Callable, *args: Any, default: Any = None, **kwargs: Any) -> Any:
    try:
        return func(*args, **kwargs)
    except (ValueError, TypeError, KeyError) as e:
        logger.error(f"Data validation error: {e}")
        return default
    except Exception as e:
        logger.critical(f"Unexpected system failure: {e}", exc_info=True)
        raise ProcessingError(f"Critical failure during {func.__name__}") from e

def validate_input(data: Optional[dict]) -> dict:
    if not isinstance(data, dict):
        raise ValueError("Input must be a dictionary")
    return data

def process_data(data: Any) -> Any:
    try:
        clean_data = validate_input(data)
        return {k: v for k, v in clean_data.items() if v is not None}
    except (ValueError, AttributeError) as e:
        logger.warning(f"Invalid input format: {e}")
        return {}
    except Exception as e:
        logger.error(f"Processing error: {e}")
        raise