import logging
from typing import Any, Callable, Dict, Optional

logger = logging.getLogger(__name__)

class BaseHandler:
    def __init__(self, registry: Optional[Dict[str, Callable]] = None):
        self._registry = registry or {}

    def register(self, name: str, func: Callable) -> None:
        self._registry[name] = func

    def execute(self, name: str, *args: Any, **kwargs: Any) -> Any:
        func = self._registry.get(name)
        if not func:
            logger.error(f'handler {name} not found')
            raise ValueError(f'unknown handler: {name}')
        return func(*args, **kwargs)

class DataHandler(BaseHandler):
    def process_payload(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            return {k: v for k, v in data.items() if v is not None}
        except Exception as e:
            logger.exception('processing error')
            raise e

def get_handler_instance() -> DataHandler:
    return DataHandler()