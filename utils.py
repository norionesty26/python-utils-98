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

def batch_process(items: list, chunk_size: int = 100):
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]

class PerformanceTimer:
    def __init__(self, name: str = "task"):
        self.name = name

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.elapsed = time.perf_counter() - self.start
        print(f"{self.name} took {self.elapsed:.4f}s")

def fast_flatten(nested_list: list) -> list:
    return [item for sublist in nested_list for item in sublist]