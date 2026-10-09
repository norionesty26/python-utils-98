import os
from typing import Any, Dict, List, Optional

def clean_dict(data: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in data.items() if v is not None}

def get_env_var(key: str, default: Optional[str] = None) -> str:
    return os.environ.get(key, default or "")

def batch_process(items: List[Any], size: int) -> List[List[Any]]:
    if size <= 0:
        raise ValueError("Batch size must be positive")
    return [items[i : i + size] for i in range(0, len(items), size)]

def safe_getattr(obj: Any, attr: str, default: Any = None) -> Any:
    try:
        return getattr(obj, attr, default)
    except AttributeError:
        return default

def flatten_list(nested: List[List[Any]]) -> List[Any]:
    return [item for sublist in nested for item in sublist]