from typing import Any, Iterable, Optional, Callable


def batch_process(data: Iterable[Any], func: Callable[[Any], Any], chunk_size: int = 100) -> list[Any]:
    """Process data in chunks to manage memory efficiency."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    results = []
    chunk = []
    for item in data:
        chunk.append(item)
        if len(chunk) == chunk_size:
            results.extend(map(func, chunk))
            chunk = []
    
    if chunk:
        results.extend(map(func, chunk))
    return results


def deep_get(data: dict[Any, Any], keys: str, default: Optional[Any] = None) -> Any:
    """Retrieve nested dictionary values using dot notation."""
    for key in keys.split('.'):
        if not isinstance(data, dict) or key not in data:
            return default
        data = data[key]
    return data


def flatten(items: Iterable[Any]) -> list[Any]:
    """Flatten nested iterables into a single list."""
    result = []
    for item in items:
        if isinstance(item, (list, tuple, set)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result