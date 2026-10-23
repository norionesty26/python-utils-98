import time
import functools
from typing import Callable, Any, Type

def retry(exceptions: tuple[Type[Exception], ...], max_retries: int = 3, delay: float = 1.0):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    time.sleep(delay * (2 ** attempt))
            raise last_exception
        return wrapper
    return decorator

class NetworkHandler:
    @retry((ConnectionError, TimeoutError), max_retries=3, delay=0.5)
    def request(self, url: str) -> str:
        # simulate network operation
        return f"response from {url}"