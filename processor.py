from typing import Any, Callable, Dict, List, Optional


def batch_process(data: List[Any], func: Callable[[Any], Any], chunk_size: int = 10) -> List[Any]:
    """Split data into chunks and process."""
    if not data or chunk_size <= 0:
        return []
    return [func(item) for chunk in [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)] for item in chunk]


def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """Flatten nested dictionary keys."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def clean_data(data: Any, target_type: type = str) -> Any:
    """Filter and cast data values."""
    if isinstance(data, list):
        return [clean_data(i, target_type) for i in data if i is not None]
    if isinstance(data, dict):
        return {k: clean_data(v, target_type) for k, v in data.items() if v is not None}
    return target_type(data) if data is not None else None