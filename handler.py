import logging
from typing import Any, Callable, Optional, Type

logger = logging.getLogger(__name__)

class ExecutionError(Exception):
    pass

def safe_execute(
    func: Callable, 
    *args: Any, 
    retries: int = 0, 
    expected_errors: tuple[Type[Exception], ...] = (Exception,)
) -> Optional[Any]:
    attempt = 0
    while attempt <= retries:
        try:
            return func(*args)
        except expected_errors as e:
            attempt += 1
            if attempt > retries:
                logger.error(f"Execution failed after {attempt} attempts: {e}")
                raise ExecutionError(f"Permanent failure in {func.__name__}") from e
            logger.warning(f"Retry {attempt}/{retries} for {func.__name__}")
    return None

def validate_input(data: Any, schema: dict) -> bool:
    try:
        if not isinstance(data, dict):
            return False
        return all(key in data for key in schema.keys())
    except (TypeError, AttributeError) as e:
        logger.debug(f"Validation error: {e}")
        return False