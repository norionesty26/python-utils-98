from typing import Any, Callable, Dict, List, Optional


class DataProcessor:
    def __init__(self, validator: Optional[Callable[[Dict[str, Any]], bool]] = None):
        self.validator = validator or self._default_validator
        self.processed_count = 0
        self.failed_count = 0

    @staticmethod
    def _default_validator(item: Dict[str, Any]) -> bool:
        if not isinstance(item, dict):
            return False
        if "id" not in item or not isinstance(item["id"], (int, str)):
            return False
        if "payload" not in item or item["payload"] is None:
            return False
        return True

    def process_batch(self, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        results = []
        for item in items:
            if not self.validator(item):
                self.failed_count += 1
                continue

            processed = self._process_single(item)
            results.append(processed)
            self.processed_count += 1

        return results

    def _process_single(self, item: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "id": item["id"],
            "status": "processed",
            "data": str(item["payload"]).strip().upper(),
        }
