import os
import json
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any] = None):
        self.config = defaults or {}

    def load_from_json(self, filepath: str) -> None:
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                self.config.update(json.load(f))

    def load_from_env(self, prefix: str = 'APP_') -> None:
        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix):].lower()
                self.config[config_key] = value

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

    @property
    def all(self) -> Dict[str, Any]:
        return self.config.copy()