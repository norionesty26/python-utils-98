import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

class DataProcessor:
    def __init__(self, settings: Optional[Dict[str, Any]] = None):
        self.settings = settings or {}

    def sanitize(self, data: Any) -> Any:
        if isinstance(data, str):
            return data.strip()
        if isinstance(data, dict):
            return {k: self.sanitize(v) for k, v in data.items()}
        if isinstance(data, list):
            return [self.sanitize(i) for i in data]
        return data

    def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        try:
            processed = self.sanitize(payload)
            logger.info("processing complete")
            return processed
        except Exception as e:
            logger.error(f"execution failure: {e}")
            raise

def get_instance(config: Optional[Dict[str, Any]] = None) -> DataProcessor:
    return DataProcessor(config)