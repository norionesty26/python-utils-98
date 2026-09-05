from typing import Any, Dict, List


class ValidationError(Exception):
    pass


def validate_record(record: Dict[str, Any]) -> bool:
    if not isinstance(record, dict):
        raise ValidationError("Record must be a dictionary")
    if "id" not in record or not isinstance(record["id"], (int, str)):
        raise ValidationError("Record must contain a valid 'id'")
    if "data" not in record:
        raise ValidationError("Record must contain a 'data' field")
    return True


def process_batch(batch: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    processed = []
    for item in batch:
        try:
            validate_record(item)
            result = {
                "id": item["id"],
                "status": "processed",
                "payload": str(item["data"]).strip().upper(),
            }
            processed.append(result)
        except ValidationError as err:
            processed.append(
                {"id": item.get("id"), "status": "failed", "error": str(err)}
            )
    return processed


def run_processor(payloads: List[Dict[str, Any]]) -> Dict[str, Any]:
    if not isinstance(payloads, list):
        raise TypeError("Input payloads must be a list")

    results = process_batch(payloads)
    success_count = sum(1 for r in results if r["status"] == "processed")
    return {
        "total": len(payloads),
        "successful": success_count,
        "failed": len(payloads) - success_count,
        "results": results,
    }
