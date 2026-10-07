import functools
import itertools
from typing import Any, Callable, Generator, Iterable, Sequence


class FastBatchProcessor:
    __slots__ = ("_batch_size", "_transform")

    def __init__(self, transform: Callable[[Any], Any], batch_size: int = 100):
        if batch_size <= 0:
            raise ValueError("batch_size must be greater than zero")
        self._batch_size = batch_size
        self._transform = transform

    def process_stream(self, items: Iterable[Any]) -> Generator[list[Any], None, None]:
        iterator = iter(items)
        while True:
            batch = list(itertools.islice(iterator, self._batch_size))
            if not batch:
                break
            yield [self._transform(item) for item in batch]

    def process_flat(self, items: Sequence[Any]) -> list[Any]:
        transform = self._transform
        return [transform(item) for item in items]


@functools.lru_cache(maxsize=1024)
def memoized_compute(key: str, cost_factor: int = 1) -> int:
    return sum(ord(char) * cost_factor for char in key)
