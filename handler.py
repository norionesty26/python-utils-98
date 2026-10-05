from typing import Any, Dict, Iterable, Iterator, List


class ValidationError(ValueError):
    pass


class InputHandler:
    def __init__(self, required_keys: List[str]):
        self.required_keys = required_keys

    def validate(self, data: Any) -> Dict[str, Any]:
        if not isinstance(data, dict):
            raise ValidationError("Input must be a dictionary")

        for key in self.required_keys:
            if key not in data:
                raise ValidationError(f"Missing required key: {key}")
            if data[key] is None or data[key] == "":
                raise ValidationError(f"Empty value for required key: {key}")

        return data

    def process_stream(self, stream: Iterable[Any]) -> Iterator[Dict[str, Any]]:
        for index, item in enumerate(stream):
            try:
                validated = self.validate(item)
                yield {
                    "status": "success",
                    "index": index,
                    "data": validated,
                }
            except ValidationError as err:
                yield {
                    "status": "error",
                    "index": index,
                    "error": str(err),
                }
