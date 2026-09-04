import json
import os
from typing import Any, Dict

def load_config(path: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    if not os.path.exists(path):
        return defaults

    try:
        with open(path, 'r') as f:
            data = json.load(f)
    except (json.JSONDecodeError, IOError):
        return defaults

    config = defaults.copy()
    config.update({k: v for k, v in data.items() if k in defaults})
    return config

def update_config(path: str, new_values: Dict[str, Any]) -> None:
    config = {}
    if os.path.exists(path):
        try:
            with open(path, 'r') as f:
                config = json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    
    config.update(new_values)
    with open(path, 'w') as f:
        json.dump(config, f, indent=4)