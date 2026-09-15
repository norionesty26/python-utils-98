import functools
import time
from typing import Callable, Any, Dict

CACHE: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in CACHE:
            CACHE[key] = func(*args, **kwargs)
        return CACHE[key]
    return wrapper

class BatchProcessor:
    def __init__(self, size: int = 100):
        self.size = size
        self.buffer = []

    def process(self, item: Any, callback: Callable) -> None:
        self.buffer.append(item)
        if len(self.buffer) >= self.size:
            callback(self.buffer)
            self.buffer.clear()

def timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        return result, end - start
    return wrapper

def fast_flatten(nested: list) -> list:
    return [item for sublist in nested for item in sublist]

def clear_cache() -> None:
    CACHE.clear()