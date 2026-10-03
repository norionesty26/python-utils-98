from typing import Any, Iterable, Dict, List, Optional

def deep_flatten(items: Iterable[Any]) -> List[Any]:
    result = []
    for item in items:
        if isinstance(item, (list, tuple, set)):
            result.extend(deep_flatten(item))
        else:
            result.append(item)
    return result

def batch_process(data: List[Any], size: int) -> Iterable[List[Any]]:
    for i in range(0, len(data), size):
        yield data[i:i + size]

def sanitize_dict(data: Dict[str, Any], keys: List[str]) -> Dict[str, Any]:
    return {k: v for k, v in data.items() if k not in keys}

def get_nested(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    keys = path.split('.')
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key)
        else:
            return default
    return data if data is not None else default