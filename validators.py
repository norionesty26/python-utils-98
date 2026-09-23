import re
from typing import Any, Optional, Union


class ValidationError(ValueError):
    """Raised when validation fails for input data."""


def validate_numeric_range(
    value: Any,
    min_val: Optional[Union[int, float]] = None,
    max_val: Optional[Union[int, float]] = None,
) -> float:
    if value is None:
        raise ValidationError("Value cannot be None")

    try:
        num = float(value)
    except (TypeError, ValueError) as err:
        raise ValidationError(f"Cannot convert {value!r} to numeric value") from err

    if min_val is not None and num < min_val:
        raise ValidationError(f"Value {num} is below minimum allowed {min_val}")
    if max_val is not None and num > max_val:
        raise ValidationError(f"Value {num} is above maximum allowed {max_val}")

    return num


def validate_email_address(email: Any) -> str:
    if not isinstance(email, str):
        raise ValidationError(f"Expected string, got {type(email).__name__}")

    cleaned = email.strip()
    if not cleaned:
        raise ValidationError("Email address cannot be empty")

    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(pattern, cleaned):
        raise ValidationError(f"Invalid email format: {cleaned!r}")

    return cleaned


def safe_parse_json_key(data: dict[str, Any], key: str, expected_type: type) -> Any:
    if not isinstance(data, dict):
        raise ValidationError(f"Expected dictionary input, got {type(data).__name__}")

    if key not in data:
        raise ValidationError(f"Missing required key: {key!r}")

    val = data[key]
    if not isinstance(val, expected_type):
        raise ValidationError(
            f"Key {key!r} must be {expected_type.__name__}, got {type(val).__name__}"
        )

    return val
