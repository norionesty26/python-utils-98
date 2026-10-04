from collections import defaultdict
from functools import wraps
from typing import Any, Callable, Dict, List, Sequence, TypeVar

T = TypeVar("T")
R = TypeVar("R")


def memoize_method(maxsize: int = 128):
    def decorator(func: Callable[..., R]) -> Callable[..., R]:
        @wraps(func)
        def wrapper(self, *args: Any, **kwargs: Any) -> R:
            key = (args, tuple(sorted(kwargs.items())))
            if not hasattr(self, "_cache"):
                self._cache: Dict[str, Any] = defaultdict(dict)
            func_cache = self._cache[func.__name__]
            if key not in func_cache:
                if len(func_cache) >= maxsize:
                    func_cache.clear()
                func_cache[key] = func(self, *args, **kwargs)
            return func_cache[key]

        return wrapper

    return decorator


class BatchExecutor:
    def __init__(self, batch_size: int = 100):
        self.batch_size = max(1, batch_size)

    def chunk_sequence(self, sequence: Sequence[T]) -> List[Sequence[T]]:
        size = self.batch_size
        return [sequence[i : i + size] for i in range(0, len(sequence), size)]

    def map_batched(self, func: Callable[[T], R], items: Sequence[T]) -> List[R]:
        results: List[R] = []
        for chunk in self.chunk_sequence(items):
            results.extend(map(func, chunk))
        return results