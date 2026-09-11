import os
import json
from typing import Any, Dict, Optional

class ConfigError(Exception):
    pass

def load_config(path: str) -> Dict[str, Any]:
    if not os.path.exists(path):
        raise ConfigError(f"config file not found: {path}")

    if not os.access(path, os.R_OK):
        raise ConfigError(f"insufficient permissions for: {path}")

    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        if not isinstance(data, dict):
            raise ConfigError("invalid config format: expected json object")
            
        return data
    except json.JSONDecodeError as e:
        raise ConfigError(f"malformed json: {e.msg}") from e
    except Exception as e:
        raise ConfigError(f"unexpected error reading config: {str(e)}") from e

def get_setting(config: Dict[str, Any], key: str, default: Optional[Any] = None) -> Any:
    try:
        return config.get(key, default)
    except AttributeError:
        return default