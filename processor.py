import random
import time
from functools import wraps
from typing import Any, Callable, Tuple, Type, TypeVar

T = TypeVar("T")


class RetryError(Exception):
    def __init__(self, last_exception: Exception, attempts: int) -> None:
        self.last_exception = last_exception
        self.attempts = attempts
        super().__init__(
            f"Operation failed after {attempts} attempts: {last_exception}"
        )


def retry(
    exceptions: Tuple[Type[Exception], ...] = (Exception,),
    max_attempts: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    jitter: bool = True,
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            current_delay = delay
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    if attempt == max_attempts:
                        raise RetryError(exc, attempts=max_attempts) from exc
                    sleep_time = current_delay
                    if jitter:
                        sleep_time += random.uniform(0, current_delay * 0.1)
                    time.sleep(sleep_time)
                    current_delay *= backoff
            raise RetryError(
                RuntimeError("Unexpected retry loop termination"),
                attempts=max_attempts,
            )

        return wrapper

    return decorator
