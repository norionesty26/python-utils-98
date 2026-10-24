import os
from typing import Any, Dict, Optional

class ConfigurationError(Exception):
    pass

def load_config(path: str) -> Dict[str, Any]:
    if not path or not isinstance(path, str):
        raise ConfigurationError("invalid configuration file path")
    
    if not os.path.exists(path):
        raise FileNotFoundError(f"config file not found: {path}")
        
    try:
        with open(path, 'r') as f:
            data = f.read()
            if not data.strip():
                return {}
            return dict(line.split('=') for line in data.splitlines() if '=' in line)
    except (IOError, ValueError) as e:
        raise ConfigurationError(f"error parsing configuration: {e}")

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    value = os.getenv(key)
    if value is None:
        if default is not None:
            return default
        raise ConfigurationError(f"missing required environment variable: {key}")
    return value