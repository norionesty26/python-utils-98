from typing import Any, Callable, Dict, List, Optional, TypeVar

T = TypeVar('T')


def compose(*functions: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """Compose multiple functions into a single pipeline."""
    def pipeline(data: Any) -> Any:
        for func in functions:
            data = func(data)
        return data
    return pipeline


def chunk_list(items: List[T], size: int) -> List[List[T]]:
    """Split a list into smaller chunks of a specified size."""
    if size <= 0:
        raise ValueError("chunk size must be greater than zero")
    return [items[i:i + size] for i in range(0, len(items), size)]


def dict_get_nested(data: Dict[str, Any], keys: List[str], default: Any = None) -> Any:
    """Retrieve nested value from dictionary using a list of keys."""
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current


def apply_defaults(config: Dict[str, Any], defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Merge a configuration dictionary with default values."""
    result = defaults.copy()
    result.update(config)
    return result