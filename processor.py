from typing import Any, Callable, Dict, List, Optional


class ValidationError(Exception):
    pass


class DataProcessor:
    def __init__(self, validator: Optional[Callable[[Any], bool]] = None) -> None:
        self.validator = validator or self._default_validator
        self.processed_count = 0
        self.errors: List[Dict[str, Any]] = []

    def _default_validator(self, item: Any) -> bool:
        if item is None:
            return False
        if isinstance(item, (int, float)) and item < 0:
            return False
        if isinstance(item, str) and not item.strip():
            return False
        return True

    def process_batch(self, items: List[Any]) -> List[Dict[str, Any]]:
        results = []
        for index, item in enumerate(items):
            if not self.validator(item):
                self.errors.append({
                    "index": index,
                    "item": item,
                    "reason": "Invalid input payload",
                })
                continue

            processed = self._process_single(item)
            results.append(processed)
            self.processed_count += 1

        return results

    def _process_single(self, item: Any) -> Dict[str, Any]:
        return {"status": "success", "value": item}
