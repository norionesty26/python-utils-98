import re
from typing import Any, Optional

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

class ValidationError(Exception):
    pass

def validate_email(email: Any) -> str:
    if not isinstance(email, str) or not EMAIL_REGEX.match(email):
        raise ValidationError(f"invalid email format: {email}")
    return email

def validate_range(value: int, min_val: int, max_val: int) -> int:
    if not (min_val <= value <= max_val):
        raise ValidationError(f"value {value} outside range [{min_val}, {max_val}]")
    return value

def validate_not_empty(value: Optional[str]) -> str:
    if not value or not value.strip():
        raise ValidationError("value cannot be empty")
    return value.strip()

def validate_schema(data: dict, schema: dict) -> bool:
    for key, validator in schema.items():
        if key not in data:
            raise ValidationError(f"missing required key: {key}")
        validator(data[key])
    return True