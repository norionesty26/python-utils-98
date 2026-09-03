import collections
from typing import Any, Iterable, Dict, List, Union

def flatten(data: Iterable, parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    items = []
    for k, v in data.items() if isinstance(data, dict) else enumerate(data):
        new_key = f"{parent_key}{sep}{k}" if parent_key else str(k)
        if isinstance(v, (dict, list)):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def chunker(data: Iterable, size: int) -> Iterable:
    for i in range(0, len(data), size):
        yield data[i:i + size]

def distinct(data: Iterable) -> List[Any]:
    return list(dict.fromkeys(data))

def sanitize(data: Dict, keys: Iterable[str]) -> Dict[str, Any]:
    return {k: v for k, v in data.items() if k not in keys}

def coalesce(*args: Any) -> Any:
    for arg in args:
        if arg is not None:
            return arg
    return None