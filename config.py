import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any] = None):
        self.defaults = defaults or {}
        self.config = self.defaults.copy()

    def load_from_file(self, filepath: str) -> None:
        if not os.path.exists(filepath):
            return
        with open(filepath, 'r') as f:
            try:
                data = json.load(f)
                self.config.update(data)
            except json.JSONDecodeError:
                pass

    def load_from_env(self, prefix: str = 'APP_') -> None:
        for key in os.environ:
            if key.startswith(prefix):
                config_key = key[len(prefix):].lower()
                self.config[config_key] = os.environ[key]

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

    def __getitem__(self, key: str) -> Any:
        return self.config[key]