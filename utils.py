import time
from functools import wraps
from typing import Callable, Any, Tuple, Type

def retry(
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
    tries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
) -> Callable:
    if tries < 1:
        raise ValueError("tries must be 1 or greater")
    if delay < 0:
        raise ValueError("delay must be 0 or greater")
    if backoff < 1:
        raise ValueError("backoff must be 1 or greater")

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt_tries = tries
            attempt_delay = delay
            while attempt_tries > 1:
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    time.sleep(attempt_delay)
                    attempt_tries -= 1
                    attempt_delay *= backoff
            return func(*args, **kwargs)
        return wrapper
    return decorator