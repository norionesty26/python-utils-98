import functools
import time
import logging
from typing import Callable, Any, Dict

def retry(attempts: int = 3, delay: float = 1.0):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_ex = None
            for _ in range(attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_ex = e
                    time.sleep(delay)
            raise last_ex
        return wrapper
    return decorator

def chunk_list(data: list, size: int):
    for i in range(0, len(data), size):
        yield data[i:i + size]

def dict_merge(base: Dict, update: Dict) -> Dict:
    result = base.copy()
    for key, value in update.items():
        if isinstance(value, dict) and key in result and isinstance(result[key], dict):
            result[key] = dict_merge(result[key], value)
        else:
            result[key] = value
    return result

def setup_logger(name: str, level: int = logging.INFO):
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(level)
    return logger