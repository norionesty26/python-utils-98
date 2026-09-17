import re
from typing import Any, Optional

def is_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def is_uuid(value: str) -> bool:
    pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
    return bool(re.match(pattern, value.lower()))

def is_not_empty(value: Optional[str]) -> bool:
    return bool(value and value.strip())

def is_within_range(value: int, min_val: int, max_val: int) -> bool:
    return min_val <= value <= max_val

def validate_dict(data: dict, schema: dict) -> bool:
    for key, expected_type in schema.items():
        if key not in data or not isinstance(data[key], expected_type):
            return False
    return True

def sanitize_input(value: Any) -> str:
    if not isinstance(value, str):
        return str(value)
    return value.strip().replace('<', '&lt;').replace('>', '&gt;')

def is_alphanumeric(value: str) -> bool:
    return value.isalnum()