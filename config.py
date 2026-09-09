import json
import os
from typing import Any, Dict, Optional

class ConfigLoader:
    def __init__(self, defaults: Optional[Dict[str, Any]] = None):
        self._config = defaults or {}

    def load_from_json(self, filepath: str) -> None:
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                self._config.update(json.load(f))

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    @property
    def all(self) -> Dict[str, Any]:
        return self._config.copy()

    def update(self, overrides: Dict[str, Any]) -> None:
        self._config.update(overrides)

def create_config(defaults: Optional[Dict[str, Any]] = None) -> ConfigLoader:
    return ConfigLoader(defaults)