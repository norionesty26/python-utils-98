import json
from pathlib import Path
from typing import Any, Dict, Union


class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any] = None) -> None:
        self.defaults = defaults or {}
        self.config = self.defaults.copy()

    def load_from_dict(self, data: Dict[str, Any]) -> None:
        self.config = self._deep_merge(self.defaults, data)

    def load_from_json(self, filepath: Union[str, Path]) -> None:
        path = Path(filepath)
        if not path.exists():
            raise FileNotFoundError(f'Configuration file not found: {filepath}')
        with path.open('r', encoding='utf-8') as f:
            data = json.load(f)
        self.load_from_dict(data)

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

    def _deep_merge(self, base: Dict[str, Any], update: Dict[str, Any]) -> Dict[str, Any]:
        merged = base.copy()
        for key, value in update.items():
            if isinstance(value, dict) and isinstance(merged.get(key), dict):
                merged[key] = self._deep_merge(merged[key], value)
            else:
                merged[key] = value
        return merged
