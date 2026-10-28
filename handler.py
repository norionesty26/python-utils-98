from typing import Any, Dict, List, Optional, Union


def deep_update(source: Dict[Any, Any], overrides: Dict[Any, Any]) -> Dict[Any, Any]:
    """Recursively updates a dictionary with nested overrides."""
    for key, value in overrides.items():
        if isinstance(value, dict) and value:
            source[key] = deep_update(source.get(key, {}), value)
        else:
            source[key] = value
    return source


def sanitize_keys(data: Any, forbidden: List[str]) -> Any:
    """Recursively removes sensitive keys from nested data structures."""
    if isinstance(data, dict):
        return {
            k: sanitize_keys(v, forbidden) for k, v in data.items() if k not in forbidden
        }
    if isinstance(data, list):
        return [sanitize_keys(item, forbidden) for item in data]
    return data


def flatten_dict(data: Dict[Any, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flattens a nested dictionary into a single-level dictionary."""
    items = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)