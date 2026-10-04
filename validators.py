import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

class ValidationError(Exception):
    pass

def validate_input(value: Any, expected_type: type, allow_none: bool = False) -> bool:
    if value is None:
        if allow_none:
            return True
        raise ValidationError('value cannot be none')
    if not isinstance(value, expected_type):
        raise ValidationError(f'expected {expected_type.__name__}, got {type(value).__name__}')
    return True

def safe_execute(func: callable, *args: Any, **kwargs: Any) -> Optional[Any]:
    try:
        return func(*args, **kwargs)
    except (ValueError, TypeError, AttributeError) as e:
        logger.error(f'execution error in {func.__name__}: {e}')
        return None
    except Exception as e:
        logger.critical(f'unhandled exception in {func.__name__}: {e}')
        raise