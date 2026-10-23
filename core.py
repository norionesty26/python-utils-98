import functools
from itertools import islice
from typing import Callable, Generator, Iterable, List, Sequence, TypeVar

T = TypeVar("T")
R = TypeVar("R")


class CorePipeline:
    __slots__ = ("_batch_size", "_cache_size")

    def __init__(self, batch_size: int = 1000, cache_size: int = 1024) -> None:
        self._batch_size = batch_size
        self._cache_size = cache_size

    def chunk_stream(self, iterable: Iterable[T]) -> Generator[List[T], None, None]:
        iterator = iter(iterable)
        while chunk := list(islice(iterator, self._batch_size)):
            yield chunk

    def fast_map(self, func: Callable[[T], R], items: Iterable[T]) -> List[R]:
        cached_func = functools.lru_cache(maxsize=self._cache_size)(func)
        return [cached_func(item) for item in items]

    def process_in_batches(
        self, func: Callable[[T], R], items: Sequence[T]
    ) -> Generator[List[R], None, None]:
        cached_func = functools.lru_cache(maxsize=self._cache_size)(func)
        for chunk in self.chunk_stream(items):
            yield [cached_func(item) for item in chunk]
