import functools
from typing import Callable, Any, Dict

class PerformanceCache:
    def __init__(self, max_size: int = 128):
        self.cache: Dict[tuple, Any] = {}
        self.max_size = max_size

    def __call__(self, func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            key = (func.__name__, args, frozenset(kwargs.items()))
            if key not in self.cache:
                if len(self.cache) >= self.max_size:
                    self.cache.pop(next(iter(self.cache)))
                self.cache[key] = func(*args, **kwargs)
            return self.cache[key]
        return wrapper

def batch_process(items: list, chunk_size: int = 100):
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]

def fast_map(func: Callable, data: list) -> list:
    return [func(x) for x in data]

def optimized_compute(data: list) -> float:
    # Minimal overhead aggregation
    return sum(map(float, data)) / len(data) if data else 0.0