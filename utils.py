import functools
import logging
import time
from typing import Any, Callable, Tuple, Type, Union

logger = logging.getLogger(__name__)


def retry(
    exceptions: Union[Type[BaseException], Tuple[Type[BaseException], ...]] = Exception,
    max_attempts: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == max_attempts:
                        raise
                    logger.warning(
                        "Attempt %d/%d failed: %s. Retrying in %.2fs...",
                        attempt,
                        max_attempts,
                        err,
                        current_delay,
                    )
                    time.sleep(current_delay)
                    current_delay *= backoff

        return wrapper

    return decorator
