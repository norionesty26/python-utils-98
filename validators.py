import re
from typing import Any, Optional

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

class ValidationError(Exception):
    pass

def validate_email(email: str) -> bool:
    if not isinstance(email, str) or not EMAIL_REGEX.match(email):
        raise ValidationError(f"invalid email format: {email}")
    return True

def validate_not_empty(value: Any, field_name: str = "field") -> Any:
    if value is None or (isinstance(value, (str, list, dict)) and not value):
        raise ValidationError(f"{field_name} cannot be empty")
    return value

def validate_range(value: int, min_val: int, max_val: int) -> int:
    if not (min_val <= value <= max_val):
        raise ValidationError(f"value {value} out of range [{min_val}, {max_val}]")
    return value

def safe_get(data: dict, key: str, default: Any = None) -> Any:
    return data.get(key, default)

def sanitize_input(value: str) -> str:
    return str(value).strip()