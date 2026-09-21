import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any] = None):
        self._config = defaults or {}

    def load_from_file(self, filepath: str) -> None:
        if not os.path.exists(filepath):
            return
        with open(filepath, 'r') as f:
            data = json.load(f)
            self._config.update(data)

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    @property
    def all(self) -> Dict[str, Any]:
        return self._config.copy()

    def update(self, new_settings: Dict[str, Any]) -> None:
        self._config.update(new_settings)

def load_config(filepath: str, defaults: Dict[str, Any] = None) -> ConfigLoader:
    loader = ConfigLoader(defaults)
    loader.load_from_file(filepath)
    return loader