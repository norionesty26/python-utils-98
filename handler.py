from typing import Any, Dict, Optional

def deep_get(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    """Retrieve nested dictionary values using dot notation."""
    keys = path.split('.')
    curr = data
    try:
        for key in keys:
            curr = curr[key]
        return curr
    except (KeyError, TypeError, AttributeError):
        return default

def sanitize_dict(data: Dict[str, Any], keys: Optional[list] = None) -> Dict[str, Any]:
    """Remove sensitive keys or filter dictionary contents."""
    if keys is None:
        keys = ['password', 'secret', 'token', 'key']
    return {k: v for k, v in data.items() if k.lower() not in keys}

def flatten_dict(data: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flatten nested dictionary into single-level structure."""
    items = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def format_data_size(value: int) -> str:
    """Human readable string for byte sizes."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if value < 1024:
            return f"{value:.2f} {unit}"
        value /= 1024
    return f"{value:.2f} PB"