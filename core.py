from functools import lru_cache, wraps
from typing import Any, Callable, Iterable, Iterator, List, TypeVar

T = TypeVar("T")


class BatchProcessor:
    def __init__(self, batch_size: int = 1000):
        if batch_size <= 0:
            raise ValueError("batch_size must be greater than 0")
        self.batch_size = batch_size

    def chunk(self, iterable: Iterable[T]) -> Iterator[List[T]]:
        batch = []
        for item in iterable:
            batch.append(item)
            if len(batch) == self.batch_size:
                yield batch
                batch = []
        if batch:
            yield batch


def memoize(maxsize: int = 128) -> Callable:
    def decorator(func: Callable) -> Callable:
        cached_func = lru_cache(maxsize=maxsize)(func)

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if kwargs:
                return cached_func(*args, tuple(sorted(kwargs.items())))
            return cached_func(*args)

        wrapper.cache_clear = cached_func.cache_clear
        wrapper.cache_info = cached_func.cache_info
        return wrapper

    return decorator


def fast_flatten(nested_iterable: Iterable[Iterable[T]]) -> List[T]:
    return [item for sublist in nested_iterable for item in sublist]
