import logging
from typing import Any, List, Optional

class DataProcessor:
    def __init__(self, items: Optional[List[Any]] = None):
        self.items = items or []
        self.logger = logging.getLogger(__name__)

    def process_batch(self) -> List[Any]:
        return [self._transform(item) for item in self.items if item is not None]

    def _transform(self, item: Any) -> Any:
        if isinstance(item, str):
            return item.strip().lower()
        if isinstance(item, (int, float)):
            return item * 2
        return item

    def clear(self) -> None:
        self.items.clear()
        self.logger.info("processor items cleared")

    def add(self, item: Any) -> None:
        self.items.append(item)

    @property
    def count(self) -> int:
        return len(self.items)