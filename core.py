import time
import functools
from typing import Callable, Any, Type, Tuple

def retry(exceptions: Tuple[Type[Exception], ...] = (Exception,), 
          attempts: int = 3, 
          delay: float = 1.0) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for i in range(attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if i < attempts - 1:
                        time.sleep(delay * (2 ** i))
            raise last_exception
        return wrapper
    return decorator