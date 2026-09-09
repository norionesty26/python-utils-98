from typing import Any, Dict, List, Optional

def flatten_dict(data: Dict[str, Any], sep: str = '_') -> Dict[str, Any]:
    items = {}
    for key, value in data.items():
        if isinstance(value, dict):
            for subkey, subvalue in flatten_dict(value, sep).items():
                items[f'{key}{sep}{subkey}'] = subvalue
        else:
            items[key] = value
    return items

def get_nested(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    keys = path.split('.')
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key)
        else:
            return default
    return data if data is not None else default

def chunk_list(data: List[Any], size: int) -> List[List[Any]]:
    if size <= 0:
        raise ValueError('Chunk size must be positive')
    return [data[i:i + size] for i in range(0, len(data), size)]

def sanitize_keys(data: Dict[str, Any], mapping: Dict[str, str]) -> Dict[str, Any]:
    return {mapping.get(k, k): v for k, v in data.items()}