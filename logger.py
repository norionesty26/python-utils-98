import logging
import functools
from typing import Callable, Any

class PerformanceLogger:
    _instances = {}

    def __new__(cls, name: str) -> logging.Logger:
        if name not in cls._instances:
            logger = logging.getLogger(name)
            if not logger.handlers:
                handler = logging.StreamHandler()
                formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
                handler.setFormatter(formatter)
                logger.addHandler(handler)
                logger.setLevel(logging.INFO)
            cls._instances[name] = logger
        return cls._instances[name]

def timed(func: Callable) -> Callable:
    @functools.lru_cache(maxsize=None)
    def _get_logger(name: str) -> logging.Logger:
        return PerformanceLogger(name)

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        logger = _get_logger(func.__module__)
        import time
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        logger.debug(f'{func.__name__} executed in {duration:.4f}s')
        return result
    return wrapper