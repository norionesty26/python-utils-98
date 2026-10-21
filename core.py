from typing import Any, Iterable, TypeVar, List
import itertools

T = TypeVar('T')

def chunk_list(data: Iterable[T], size: int) -> Iterable[List[T]]:
    iterator = iter(data)
    for first in iterator:
        yield [first] + list(itertools.islice(iterator, size - 1))

def flatten(nested_list: Iterable[Iterable[T]]) -> List[T]:
    return [item for sublist in nested_list for item in sublist]

def get_deep(data: dict, keys: str, default: Any = None) -> Any:
    curr = data
    try:
        for key in keys.split('.'):
            curr = curr[key]
        return curr
    except (KeyError, TypeError):
        return default

def distinct(data: Iterable[T]) -> List[T]:
    return list(dict.fromkeys(data))

def dict_filter(data: dict, keys: Iterable[str]) -> dict:
    return {k: v for k, v in data.items() if k in keys}

def coalesce(*args: Any) -> Any:
    return next((arg for arg in args if arg is not None), None)