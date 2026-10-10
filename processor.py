import logging
from typing import Any, Dict, List, Tuple

logger = logging.getLogger(__name__)


class ValidationError(Exception):
    pass


def validate_item(item: Any) -> Dict[str, Any]:
    if not isinstance(item, dict):
        raise ValidationError(f"Expected dict input, got {type(item).__name__}")

    if "id" not in item:
        raise ValidationError("Missing required field 'id'")

    if "value" not in item:
        raise ValidationError("Missing required field 'value'")

    if not isinstance(item["value"], (int, float)):
        raise ValidationError(f"Invalid value type: {type(item['value']).__name__}")

    return item


def process_batch(items: List[Any]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    successful = []
    failed = []

    for idx, raw_item in enumerate(items):
        try:
            validated = validate_item(raw_item)
            processed_data = {
                "id": validated["id"],
                "processed_value": round(float(validated["value"]), 2),
                "status": "success",
            }
            successful.append(processed_data)
        except ValidationError as err:
            logger.warning(f"Validation failed at index {idx}: {err}")
            failed.append({"index": idx, "raw": raw_item, "error": str(err)})
        except Exception as err:
            logger.error(f"Unexpected error processing index {idx}: {err}")
            failed.append({"index": idx, "raw": raw_item, "error": f"Internal error: {err}"})

    return successful, failed
