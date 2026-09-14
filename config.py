import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any] = None):
        self.defaults = defaults or {}

    def load(self, path: str) -> Dict[str, Any]:
        config = self.defaults.copy()
        if os.path.exists(path):
            try:
                with open(path, 'r') as f:
                    file_data = json.load(f)
                    config.update(file_data)
            except (json.JSONDecodeError, IOError):
                pass
        return config

    def get_env_override(self, key: str, default: Any = None) -> Any:
        return os.environ.get(key, default)

    @staticmethod
    def save(path: str, data: Dict[str, Any]) -> None:
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)