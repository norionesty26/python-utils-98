import logging
from typing import Any, Dict, List, Tuple

logger = logging.getLogger("processor")


class ValidationError(Exception):
    pass


class DataProcessor:
    def __init__(self, schema: Dict[str, type]):
        self.schema = schema

    def validate_record(self, record: Dict[str, Any]) -> None:
        for key, expected_type in self.schema.items():
            if key not in record:
                raise ValidationError(f"Missing required field: {key}")
            if not isinstance(record[key], expected_type):
                raise ValidationError(
                    f"Invalid type for {key}: expected {expected_type.__name__}, "
                    f"got {type(record[key]).__name__}"
                )

    def process_stream(
        self, records: List[Dict[str, Any]]
    ) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
        valid_records = []
        invalid_records = []

        for record in records:
            try:
                self.validate_record(record)
                valid_records.append(record)
            except ValidationError as exc:
                logger.warning("Record validation rejected: %s", exc)
                invalid_records.append(record)

        return valid_records, invalid_records