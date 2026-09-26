import os
from typing import Any, Dict, Optional

class Config:
    _settings: Dict[str, Any] = {}

    @classmethod
    def load_env(cls, prefix: str = "APP_") -> None:
        for key, value in os.environ.items():
            if key.startswith(prefix):
                cls._settings[key[len(prefix):].lower()] = value

    @classmethod
    def get(cls, key: str, default: Optional[Any] = None) -> Any:
        return cls._settings.get(key, default)

    @classmethod
    def set(cls, key: str, value: Any) -> None:
        cls._settings[key] = value

    @classmethod
    def reset(cls) -> None:
        cls._settings.clear()

    @property
    def all(self) -> Dict[str, Any]:
        return self._settings.copy()