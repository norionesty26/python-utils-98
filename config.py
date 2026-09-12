import os
import json
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "host": "127.0.0.1",
    "port": 8000,
    "debug": False,
    "timeout": 30
}

class ConfigLoader:
    def __init__(self, filepath: str = None):
        self.config = DEFAULT_CONFIG.copy()
        if filepath and os.path.exists(filepath):
            self.load_from_file(filepath)
        self.load_from_env()

    def load_from_file(self, filepath: str) -> None:
        try:
            with open(filepath, "r") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    self.config.update(data)
        except (json.JSONDecodeError, OSError):
            pass

    def load_from_env(self) -> None:
        for key in self.config:
            env_key = f"APP_{key.upper()}"
            if env_key in os.environ:
                val = os.environ[env_key]
                default_val = self.config[key]
                if isinstance(default_val, bool):
                    self.config[key] = val.lower() in ("true", "1", "yes")
                elif isinstance(default_val, int):
                    try:
                        self.config[key] = int(val)
                    except ValueError:
                        pass
                else:
                    self.config[key] = val

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)