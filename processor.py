import time
import functools
from typing import Callable, Any, Type, Tuple

def retry(exceptions: Tuple[Type[Exception], ...], 
          retries: int = 3, 
          delay: float = 1.0, 
          backoff: float = 2.0) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for i in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    if i == retries - 1:
                        raise
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

class NetworkProcessor:
    @retry(exceptions=(ConnectionError, TimeoutError), retries=3)
    def fetch_data(self, url: str) -> str:
        # Simulate network logic
        return f"data from {url}"