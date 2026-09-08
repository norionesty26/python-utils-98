import json
import os
from typing import Any, Dict, Optional


class Config:
    def __init__(
        self, defaults: Optional[Dict[str, Any]] = None, env_prefix: str = ""
    ):
        self._config: Dict[str, Any] = defaults.copy() if defaults else {}
        self.env_prefix = env_prefix

    def load_from_file(self, filepath: str) -> None:
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Config file not found: {filepath}")

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, dict):
                raise ValueError("Configuration file must contain a JSON object")
            self._config.update(data)

    def load_from_env(self) -> None:
        for key in self._config:
            env_key = f"{self.env_prefix}{key.upper()}"
            if env_key in os.environ:
                val = os.environ[env_key]
                try:
                    self._config[key] = json.loads(val)
                except json.JSONDecodeError:
                    self._config[key] = val

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self._config[key] = value

    @property
    def data(self) -> Dict[str, Any]:
        return self._config.copy()