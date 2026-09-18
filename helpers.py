import json
from typing import Any, Dict, Optional, Union

def normalize_data(data: Any) -> Any:
    if isinstance(data, dict):
        return {str(k): normalize_data(v) for k, v in data.items()}
    if isinstance(data, (list, tuple, set)):
        return [normalize_data(i) for i in data]
    return data

def safe_json_load(content: str, default: Optional[Dict] = None) -> Any:
    try:
        return json.loads(content)
    except (json.JSONDecodeError, TypeError):
        return default if default is not None else {}

def chunk_list(data: list, size: int):
    for i in range(0, len(data), size):
        yield data[i:i + size]

def extract_nested(data: Dict, keys: list, default: Any = None) -> Any:
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current