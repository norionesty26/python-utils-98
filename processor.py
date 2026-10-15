from typing import Any, Dict, List, Optional

class DataProcessor:
    def __init__(self, data: Optional[List[Dict[str, Any]]] = None):
        self.data = data or []

    def clean_records(self) -> List[Dict[str, Any]]:
        return [record for record in self.data if record and isinstance(record, dict)]

    def extract_keys(self, keys: List[str]) -> List[Dict[str, Any]]:
        return [{k: r[k] for k in keys if k in r} for r in self.clean_records()]

    def sort_by_key(self, key: str, reverse: bool = False) -> List[Dict[str, Any]]:
        return sorted(self.data, key=lambda x: x.get(key, 0), reverse=reverse)

    @staticmethod
    def validate_schema(data: List[Dict[str, Any]], required_keys: List[str]) -> bool:
        return all(all(k in record for k in required_keys) for record in data)

def process_batch(items: List[Dict[str, Any]], key: str) -> List[Any]:
    processor = DataProcessor(items)
    return [item.get(key) for item in processor.clean_records() if key in item]