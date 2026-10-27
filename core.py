import functools
import random
import time
from typing import Any, Callable, Tuple, Type


def retry(
    max_retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    jitter: bool = True,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == max_retries:
                        raise err
                    sleep_time = current_delay
                    if jitter:
                        sleep_time += random.uniform(0, current_delay * 0.1)
                    time.sleep(sleep_time)
                    current_delay *= backoff

        return wrapper

    return decorator
