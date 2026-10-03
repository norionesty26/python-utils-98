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

class DataProcessor:
    __slots__ = ('data', 'timestamp')

    def __init__(self, data: list):
        self.data = data
        self.timestamp = time.monotonic()

    def process_batch(self, factor: int) -> list:
        return [x * factor for x in self.data]

def optimized_sum(numbers: list) -> float:
    return sum(numbers)

def clear_cache() -> None:
    CACHE.clear()