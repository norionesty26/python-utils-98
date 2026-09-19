import json
import os
from typing import Any, Dict, Optional


class ConfigLoader:
    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        self._config: Dict[str, Any] = defaults.copy() if defaults else {}

    def load_dict(self, data: Dict[str, Any]) -> None:
        self._config.update(data)

    def load_json(self, filepath: str) -> None:
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    self._config.update(data)

    def load_env(self, prefix: str = "") -> None:
        for key, value in os.environ.items():
            if prefix and not key.startswith(prefix):
                continue
            config_key = key[len(prefix):].lower()
            self._config[config_key] = value

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    def as_dict(self) -> Dict[str, Any]:
        return self._config.copy()

    def __getitem__(self, key: str) -> Any:
        return self._config[key]
