import collections.abc
from typing import Any, Dict, List, Union

def deep_merge(base: Dict[Any, Any], update: Dict[Any, Any]) -> Dict[Any, Any]:
    for key, value in update.items():
        if isinstance(value, collections.abc.Mapping) and value:
            returned = deep_merge(base.get(key, {}), value)
            base[key] = returned
        else:
            base[key] = update[key]
    return base

def sanitize_keys(data: Dict[Any, Any], transform: callable) -> Dict[Any, Any]:
    return {transform(k): v for k, v in data.items()}

def flatten_dict(d: Dict[Any, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    items: List[Any] = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, collections.abc.Mapping):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def filter_none(data: Union[Dict, List]) -> Union[Dict, List]:
    if isinstance(data, dict):
        return {k: filter_none(v) for k, v in data.items() if v is not None}
    if isinstance(data, list):
        return [filter_none(i) for i in data if i is not None]
    return data