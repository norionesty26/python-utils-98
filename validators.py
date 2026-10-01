import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

class ValidationError(Exception):
    """Custom exception for input validation failures."""

def validate_payload(data: Any, schema: Dict[str, type]) -> bool:
    """Validates dictionary keys and types against a schema."""
    if not isinstance(data, dict):
        raise ValidationError(f"Expected dict, got {type(data).__name__}")

    for key, expected_type in schema.items():
        if key not in data:
            raise ValidationError(f"Missing required key: {key}")
        if not isinstance(data[key], expected_type):
            raise ValidationError(
                f"Invalid type for {key}: expected {expected_type.__name__}, "
                f"got {type(data[key]).__name__}"
            )
    return True

def process_safe(data: Any, schema: Dict[str, type], func: callable) -> Optional[Any]:
    """Wrapper to process data with input validation."""
    try:
        if validate_payload(data, schema):
            return func(data)
    except ValidationError as e:
        logger.error(f"Validation failed: {e}")
        return None
    return None