from typing import Any, Dict, Optional, Callable

class DataHandler:
    """Base handler for processing structured data streams."""

    def __init__(self, callback: Optional[Callable[[Dict[str, Any]], None]] = None) -> None:
        self.callback = callback
        self.data: Dict[str, Any] = {}

    def update(self, key: str, value: Any) -> None:
        """Update internal state and trigger optional callback."""
        self.data[key] = value
        if self.callback:
            self.callback(self.data)

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieve value by key with optional default fallback."""
        return self.data.get(key, default)

    def clear(self) -> None:
        """Reset internal storage to empty state."""
        self.data.clear()

def process_payload(data: Dict[str, Any], validator: Callable[[Any], bool]) -> Dict[str, Any]:
    """Filter dictionary contents based on a provided validation function."""
    return {k: v for k, v in data.items() if validator(v)}