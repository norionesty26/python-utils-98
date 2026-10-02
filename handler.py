import json
from typing import Any, Dict, Optional

def safe_json_load(data: str, default: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Parses JSON string into dictionary with fallback."""
    try:
        return json.loads(data)
    except (json.JSONDecodeError, TypeError):
        return default or {}

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flattens nested dictionary structure."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def sanitize_data(data: Dict[str, Any], keys_to_remove: list) -> Dict[str, Any]:
    """Removes sensitive keys from dictionary."""
    return {k: v for k, v in data.items() if k not in keys_to_remove}