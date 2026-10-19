from functools import lru_cache
import re

@lru_cache(maxsize=1024)
def is_valid_email(email: str) -> bool:
    if not email or '@' not in email:
        return False
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

@lru_cache(maxsize=512)
def sanitize_input(data: str) -> str:
    if not isinstance(data, str):
        return str(data)
    return data.strip().replace('<', '&lt;').replace('>', '&gt;')

def batch_validate(items: list, validator: callable) -> list:
    return [item for item in items if validator(item)]