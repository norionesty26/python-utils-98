from typing import Any, Dict, Generator, Iterable, List, TypeVar

T = TypeVar("T")


def deep_merge(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merges dict2 into dict1 and returns a new dictionary."""
    result = dict1.copy()
    for key, value in dict2.items():
        if isinstance(value, dict) and key in result and isinstance(result[key], dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def chunk_iterable(iterable: Iterable[T], size: int) -> Generator[List[T], None, None]:
    """Yield successive n-sized chunks from an iterable."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    chunk: List[T] = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def safe_cast(val: Any, to_type: type, default: Any = None) -> Any:
    """Safely casts a value to a specified type, returning default on failure."""
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default
