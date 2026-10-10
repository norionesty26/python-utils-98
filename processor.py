from typing import Any, Iterable, Callable, TypeVar

T = TypeVar('T')


def chunker(iterable: Iterable[T], size: int) -> Iterable[list[T]]:
    args = [iter(iterable)] * size
    return ([e for e in t if e is not None] for t in zip(*args))


def flatten(nested: Iterable[Iterable[T]]) -> list[T]:
    return [item for sublist in nested for item in sublist]


def compose(*functions: Callable[[Any], Any]) -> Callable[[Any], Any]:
    def inner(arg: Any) -> Any:
        for func in functions:
            arg = func(arg)
        return arg
    return inner


def unique(items: Iterable[T]) -> list[T]:
    return list(dict.fromkeys(items))


def batch_process(items: Iterable[T], func: Callable[[T], Any], size: int = 10) -> list[Any]:
    results = []
    for batch in chunker(items, size):
        results.extend([func(item) for item in batch])
    return results