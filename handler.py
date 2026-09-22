import logging
from typing import Any, Callable, Optional

logger = logging.getLogger(__name__)

class ExecutionHandler:
    def __init__(self, fallback: Any = None):
        self.fallback = fallback

    def safe_execute(self, func: Callable, *args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        except (ValueError, TypeError, AttributeError) as e:
            logger.error(f"Data processing error: {e}")
            return self.fallback
        except Exception as e:
            logger.critical(f"Unexpected system failure: {e}")
            raise

def validate_input(data: Any) -> bool:
    if data is None:
        return False
    if isinstance(data, (dict, list)) and not data:
        return False
    return True

def process_safe(func: Callable, data: Any, default: Any = None) -> Any:
    if not validate_input(data):
        return default
    handler = ExecutionHandler(fallback=default)
    return handler.safe_execute(func, data)