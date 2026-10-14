import re
from typing import Any, Optional

def is_email(value: str) -> bool:
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, value))

def is_uuid(value: str) -> bool:
    pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
    return bool(re.match(pattern, value, re.IGNORECASE))

def validate_range(value: int, min_val: int, max_val: int) -> bool:
    return min_val <= value <= max_val

def is_not_empty(value: Optional[str]) -> bool:
    return bool(value and value.strip())

def sanitize_input(value: str) -> str:
    return re.sub(r'[^a-zA-Z0-9\s]', '', value)