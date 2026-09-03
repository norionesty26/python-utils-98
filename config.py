import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any] = None):
        self._defaults = defaults or {}
        self._config = self._defaults.copy()

    def load_from_json(self, file_path: str) -> None:
        if not os.path.exists(file_path):
            return
        with open(file_path, 'r') as f:
            data = json.load(f)
            self._config.update(data)

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    def __getitem__(self, key: str) -> Any:
        return self._config[key]

    def __repr__(self) -> str:
        return f"ConfigLoader(config={self._config})"