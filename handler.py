import logging
from typing import Any, Callable, Dict

logger = logging.getLogger(__name__)

class RequestHandler:
    def __init__(self, registry: Dict[str, Callable]) -> None:
        self._registry = registry

    def process(self, action: str, data: Any) -> Any:
        handler = self._registry.get(action)
        if not handler:
            logger.error(f"no handler registered for: {action}")
            raise ValueError(f"unsupported action: {action}")

        try:
            return handler(data)
        except Exception as e:
            logger.exception(f"execution failed for {action}: {e}")
            raise

    @staticmethod
    def validate_payload(data: Any) -> bool:
        return isinstance(data, dict) and len(data) > 0

def create_handler(routes: Dict[str, Callable]) -> RequestHandler:
    return RequestHandler(routes)