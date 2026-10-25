import json
import os
from typing import Any, Dict, Optional


class Config:
    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        self._config: Dict[str, Any] = {}
        if defaults:
            self._config.update(defaults)

    def load_dict(self, data: Dict[str, Any]) -> "Config":
        self._config.update(data)
        return self

    def load_json(self, filepath: str) -> "Config":
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    self._config.update(data)
        return self

    def load_env(self, prefix: str = "") -> "Config":
        for key, value in os.environ.items():
            if prefix and not key.startswith(prefix):
                continue
            config_key = key[len(prefix) :].lower()
            if config_key:
                self._config[config_key] = value
        return self

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self._config[key] = value

    def to_dict(self) -> Dict[str, Any]:
        return self._config.copy()

    def __getitem__(self, key: str) -> Any:
        return self._config[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self._config[key] = value

    def __contains__(self, key: str) -> bool:
        return key in self._config
