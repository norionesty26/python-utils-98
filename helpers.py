from typing import Any, Iterable, Optional

def flatten(items: Iterable[Any]) -> list[Any]:
    """Flatten a nested list structure into a single list."""
    result = []
    for item in items:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

def get_nested(data: dict[str, Any], path: str, default: Optional[Any] = None) -> Any:
    """Retrieve a value from a nested dictionary using a dot-notation string."""
    keys = path.split('.')
    curr = data
    try:
        for key in keys:
            curr = curr[key]
        return curr
    except (KeyError, TypeError):
        return default

def chunker(items: Iterable[Any], size: int) -> Iterable[list[Any]]:
    """Split an iterable into chunks of the specified size."""
    items = list(items)
    for i in range(0, len(items), size):
        yield items[i : i + size]