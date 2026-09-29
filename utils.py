import time
import functools
from typing import Callable, Any, Type, Tuple

def retry(exceptions: Tuple[Type[Exception], ...] = (Exception,), 
          tries: int = 3, 
          delay: float = 1.0, 
          backoff: float = 2.0) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_tries, current_delay = tries, delay
            while current_tries > 1:
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    time.sleep(current_delay)
                    current_tries -= 1
                    current_delay *= backoff
            return func(*args, **kwargs)
        return wrapper
    return decorator