import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

class DataHandler:
    def __init__(self, settings: Optional[Dict[str, Any]] = None):
        self.settings = settings or {}

    def process(self, data: Any) -> Any:
        if not data:
            logger.warning("empty data received")
            return None
        try:
            return self._transform(data)
        except Exception as e:
            logger.error(f"processing error: {e}")
            raise

    def _transform(self, data: Any) -> Any:
        if isinstance(data, dict):
            return {k: str(v).strip() for k, v in data.items()}
        return str(data).strip()

def initialize_handler(config: Dict[str, Any]) -> DataHandler:
    return DataHandler(settings=config)