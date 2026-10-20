import os
from typing import Any, Optional

class ConfigError(Exception):
    pass

def get_env_variable(key: str, default: Optional[Any] = None) -> Any:
    try:
        return os.environ[key]
    except KeyError:
        if default is not None:
            return default
        raise ConfigError(f"missing required environment variable: {key}")

def load_config(keys: list[str]) -> dict[str, Any]:
    config = {}
    for key in keys:
        try:
            config[key] = get_env_variable(key)
        except ConfigError as e:
            config[key] = None
    return config

def validate_port(port: Any) -> int:
    try:
        port_int = int(port)
        if not (1 <= port_int <= 65535):
            raise ValueError
        return port_int
    except (TypeError, ValueError):
        raise ConfigError(f"invalid port number: {port}")