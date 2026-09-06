import time
from functools import wraps
from typing import Callable, Any, Tuple, Type


def retry(
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
    tries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
) -> Callable:
    """Decorator to retry a function call with exponential backoff."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt_delay = delay
            for attempt in range(1, tries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == tries:
                        raise e
                    time.sleep(attempt_delay)
                    attempt_delay *= backoff
        return wrapper
    return decorator
