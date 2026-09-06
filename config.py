import json
import os
from typing import Any, Dict, Optional


class ConfigLoader:
    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        self.defaults = defaults or {}
        self.config = self.defaults.copy()

    def load_from_dict(self, data: Dict[str, Any]) -> None:
        self.config.update(data)

    def load_from_json(self, filepath: str) -> None:
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    self.load_from_dict(data)

    def load_from_env(self, prefix: str = "") -> None:
        for key in self.defaults:
            env_key = f"{prefix}{key.upper()}"
            if env_key in os.environ:
                default_val = self.defaults[key]
                env_val = os.environ[env_key]
                self.config[key] = self._cast_value(env_val, default_val)

    def _cast_value(self, val: str, default_val: Any) -> Any:
        if isinstance(default_val, bool):
            return val.lower() in ("true", "1", "yes")
        if isinstance(default_val, int):
            return int(val)
        if isinstance(default_val, float):
            return float(val)
        return val

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)
