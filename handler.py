import time
import functools
from typing import Callable, Any, Type

def retry(exceptions: tuple[Type[Exception], ...], tries: int = 3, delay: float = 1.0, backoff: float = 2.0):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return func(*args, **kwargs)
        return wrapper
    return decorator

@retry(exceptions=(ConnectionError, TimeoutError), tries=3, delay=2)
def fetch_data(url: str) -> str:
    # Simulate network operation
    return f"response from {url}"