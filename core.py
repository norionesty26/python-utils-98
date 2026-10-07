import logging
from typing import Any, Callable, Optional, TypeVar, Union

T = TypeVar('T')

logger = logging.getLogger(__name__)

class ExecutionError(Exception):
    pass

def safe_execute(func: Callable[..., T], *args: Any, **kwargs: Any) -> Optional[T]:
    try:
        return func(*args, **kwargs)
    except (ValueError, TypeError, AttributeError, KeyError) as e:
        logger.error(f'Validation error during execution: {e}')
    except Exception as e:
        logger.critical(f'Unexpected system failure: {e}', exc_info=True)
    return None

def validate_input(data: Any, expected_type: type) -> bool:
    if data is None:
        return False
    if not isinstance(data, expected_type):
        logger.warning(f'Input type mismatch: expected {expected_type}, got {type(data)}')
        return False
    return True

def process_data(data: Any, transform: Callable[[Any], T]) -> Optional[T]:
    if not validate_input(data, (str, int, float, dict, list)):
        return None
    return safe_execute(transform, data)