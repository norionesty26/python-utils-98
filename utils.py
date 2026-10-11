import json
import os
from typing import Any, Dict, Optional

def read_json(filepath: str) -> Dict[str, Any]:
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r') as f:
        return json.load(f)

def write_json(filepath: str, data: Dict[str, Any]) -> None:
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def ensure_dir(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)

def get_env_variable(key: str, default: Optional[str] = None) -> Optional[str]:
    return os.environ.get(key, default)

def chunk_list(data: list, size: int):
    for i in range(0, len(data), size):
        yield data[i:i + size]

def flatten_dict(d: dict, parent_key: str = '', sep: str = '_') -> dict:
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)