import json
import os
from typing import Any, Dict, Optional

def load_json(filepath: str) -> Dict[str, Any]:
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(filepath: str, data: Dict[str, Any]) -> None:
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def get_env_var(key: str, default: Optional[str] = None) -> str:
    return os.getenv(key, default) or ''

def chunk_list(data: list, size: int):
    for i in range(0, len(data), size):
        yield data[i:i + size]

def flatten_dict(d: Dict, parent_key: str = '', sep: str = '_') -> Dict:
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)