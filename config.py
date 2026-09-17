import os
from typing import Any, Dict, Optional, Union


class ConfigManager:
    """Manages application configuration settings with environment overrides."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        """Initialize the configuration manager with default key-value pairs."""
        self._config: Dict[str, Any] = defaults.copy() if defaults else {}

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key, returning a default if missing."""
        return self._config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set a configuration key to a specific value."""
        self._config[key] = value

    def load_from_env(self, prefix: str = "") -> None:
        """Load environment variables matching a prefix into configuration."""
        for env_key, env_value in os.environ.items():
            if env_key.startswith(prefix):
                config_key = env_key[len(prefix):].lower()
                self._config[config_key] = self._parse_value(env_value)

    def load_from_dict(self, data: Dict[str, Any]) -> None:
        """Merge dictionary key-value pairs into current configuration."""
        self._config.update(data)

    @staticmethod
    def _parse_value(value: str) -> Union[int, float, bool, str]:
        """Cast string environment variable values into appropriate types."""
        val_lower = value.lower()
        if val_lower in ("true", "1", "yes"):
            return True
        if val_lower in ("false", "0", "no"):
            return False
        try:
            return int(value)
        except ValueError:
            pass
        try:
            return float(value)
        except ValueError:
            pass
        return value
