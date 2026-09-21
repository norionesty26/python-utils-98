"""Validation utilities for common data types and structures."""

import re
from typing import Any, Dict, List, Optional, Type, TypeVar

T = TypeVar("T")

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")


def is_email(value: str) -> bool:
    """Validate if a given string is a valid email address."""
    if not isinstance(value, str):
        return False
    return bool(EMAIL_REGEX.match(value))


def is_type(value: Any, expected_type: Type[T]) -> bool:
    """Check if a value matches the expected type."""
    return isinstance(value, expected_type)


def validate_dict_keys(
    data: Dict[str, Any],
    required_keys: List[str],
    optional_keys: Optional[List[str]] = None,
) -> bool:
    """Ensure dictionary contains required keys and no unexpected keys."""
    if not isinstance(data, dict):
        return False

    keys = set(data.keys())
    req_set = set(required_keys)

    if not req_set.issubset(keys):
        return False

    if optional_keys is not None:
        allowed_keys = req_set | set(optional_keys)
        if not keys.issubset(allowed_keys):
            return False

    return True


def in_range(
    val: Any,
    min_val: Optional[float] = None,
    max_val: Optional[float] = None,
) -> bool:
    """Check if a numeric value falls within an optional inclusive range."""
    if not isinstance(val, (int, float)):
        return False
    if min_val is not None and val < min_val:
        return False
    if max_val is not None and val > max_val:
        return False
    return True
