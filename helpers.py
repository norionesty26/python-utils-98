import collections
from typing import Any, Iterable, Dict, List, Optional

def flatten(items: Iterable[Any], depth: int = 1) -> List[Any]:
    result = []
    for item in items:
        if depth > 0 and isinstance(item, (list, tuple)):
            result.extend(flatten(item, depth - 1))
        else:
            result.append(item)
    return result

def chunker(items: Iterable[Any], size: int) -> Iterable[List[Any]]:
    items = list(items)
    for i in range(0, len(items), size):
        yield items[i : i + size]

def dict_get_path(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    keys = path.split('.')
    current = data
    try:
        for key in keys:
            current = current[key]
        return current
    except (KeyError, TypeError):
        return default

def unique_preserve_order(items: Iterable[Any]) -> List[Any]:
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result