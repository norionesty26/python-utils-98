import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any] = None):
        self.config = defaults or {}

    def load_from_env(self, prefix: str = "APP_") -> None:
        for key, value in os.environ.items():
            if key.startswith(prefix):
                clean_key = key[len(prefix):].lower()
                self.config[clean_key] = value

    def load_from_json(self, path: str) -> None:
        if os.path.exists(path):
            with open(path, "r") as f:
                self.config.update(json.load(f))

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

    def __getitem__(self, key: str) -> Any:
        return self.config[key]

    def __repr__(self) -> str:
        return f"ConfigLoader(keys={list(self.config.keys())})"