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

def batch_process(items: list, size: int):
    for i in range(0, len(items), size):
        yield items[i:i + size]

class PerformanceTimer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.duration = time.perf_counter() - self.start

def fast_flatten(data: list) -> list:
    return [item for sublist in data for item in sublist]

def singleton(cls):
    instances = {}
    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance