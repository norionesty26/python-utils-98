import os
from typing import Any, Iterable, Optional

def ensure_dir(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

def flatten(items: Iterable[Any]) -> list[Any]:
    result = []
    for item in items:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

def get_env_var(key: str, default: Optional[str] = None) -> str:
    return os.getenv(key, default) or ''

def chunk_list(data: list[Any], size: int) -> Iterable[list[Any]]:
    for i in range(0, len(data), size):
        yield data[i:i + size]

def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance