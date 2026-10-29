import logging
from typing import Any, Dict, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataHandler:
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.data: Dict[str, Any] = {}

    def update(self, key: str, value: Any) -> None:
        if not isinstance(key, str):
            raise ValueError("key must be a string")
        self.data[key] = value
        logger.info(f"Updated key: {key}")

    def get(self, key: str) -> Any:
        return self.data.get(key)

    def clear(self) -> None:
        self.data.clear()
        logger.info("Handler state cleared")

    def bulk_process(self, items: Dict[str, Any]) -> None:
        for k, v in items.items():
            self.update(k, v)

def initialize_handler(config: Optional[Dict[str, Any]] = None) -> DataHandler:
    return DataHandler(config)