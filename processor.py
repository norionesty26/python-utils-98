import logging

class DataProcessor:
    def __init__(self, schema=None):
        self.schema = schema or {}

    def validate_input(self, data):
        if not isinstance(data, dict):
            raise ValueError("input must be a dictionary")
        for key, expected_type in self.schema.items():
            if key not in data:
                raise KeyError(f"missing required key: {key}")
            if not isinstance(data[key], expected_type):
                raise TypeError(f"invalid type for {key}: expected {expected_type.__name__}")

    def process_batch(self, items):
        results = []
        for item in items:
            try:
                self.validate_input(item)
                results.append(self._execute(item))
            except (ValueError, KeyError, TypeError) as e:
                logging.error(f"validation failed: {e}")
                continue
        return results

    def _execute(self, data):
        return data.get("value", 0) * 2

def main():
    schema = {"id": int, "value": int}
    processor = DataProcessor(schema)
    payload = [
        {"id": 1, "value": 10},
        {"id": 2, "value": "invalid"},
        {"id": 3},
        "invalid_item"
    ]
    output = processor.process_batch(payload)
    print(f"processed {len(output)} items")

if __name__ == "__main__":
    main()