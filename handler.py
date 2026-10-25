import logging
from typing import Any, Callable, Dict, Optional

logger = logging.getLogger(__name__)

class BaseHandler:
    def __init__(self, settings: Optional[Dict[str, Any]] = None):
        self.settings = settings or {}

    def execute(self, func: Callable, *args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Execution error: {e}")
            raise

class DataHandler(BaseHandler):
    def process(self, data: Any) -> Any:
        if not data:
            raise ValueError("Empty input data")
        return self.execute(self._transform, data)

    def _transform(self, data: Any) -> Any:
        return str(data).strip().lower()

class ResultHandler(BaseHandler):
    def save(self, data: Any) -> bool:
        if self.settings.get("readonly"):
            return False
        logger.info("Saving data to persistence layer")
        return True