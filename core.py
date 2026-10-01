import functools
from typing import Any, Callable, Dict

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
    def __init__(self, data: list):
        self._data = data

    @memoize
    def process_batch(self, factor: int) -> list:
        return [x * factor for x in self._data]

    def clear_cache(self) -> None:
        CACHE.clear()

def batch_transform(items: list, operation: Callable) -> list:
    return list(map(operation, items))

if __name__ == '__main__':
    processor = DataProcessor(list(range(1000)))
    print(processor.process_batch(2))