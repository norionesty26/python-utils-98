import re
from datetime import datetime
from typing import Any

def is_valid_email(email: str) -> bool:
    if not isinstance(email, str) or not email:
        return False
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def is_valid_url(url: str) -> bool:
    if not isinstance(url, str) or not url:
        return False
    pattern = r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$'
    return bool(re.match(pattern, url))

def is_valid_phone(phone: str) -> bool:
    if not isinstance(phone, str) or not phone:
        return False
    cleaned = re.sub(r'[\s\-\(\)]', '', phone)
    pattern = r'^\+?\d{7,15}$'
    return bool(re.match(pattern, cleaned))

def is_valid_ipv4(ip: str) -> bool:
    if not isinstance(ip, str) or not ip:
        return False
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True

def is_valid_credit_card(number: str) -> bool:
    if not isinstance(number, str):
        return False
    digits = re.sub(r'\D', '', number)
    if len(digits) < 13 or len(digits) > 19:
        return False
    total = 0
    reverse_digits = digits[::-1]
    for i, d in enumerate(reverse_digits):
        n = int(d)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0

def is_valid_date(date_str: str, fmt: str = '%Y-%m-%d') -> bool:
    if not isinstance(date_str, str):
        return False
    try:
        datetime.strptime(date_str, fmt)
        return True
    except ValueError:
        return False

def is_positive_number(value: Any) -> bool:
    try:
        num = float(value)
        return num > 0
    except (ValueError, TypeError):
        return False

def is_non_empty(value: Any) -> bool:
    if isinstance(value, str):
        return len(value.strip()) > 0
    return value is not None and value != []

def is_alphanumeric(value: str) -> bool:
    if not isinstance(value, str):
        return False
    return bool(re.match(r'^[a-zA-Z0-9]+$', value))