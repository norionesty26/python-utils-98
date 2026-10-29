import logging
from functools import lru_cache

class PerformanceLogger:
    def __init__(self, name: str = "app_logger"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(handler)

    @lru_cache(maxsize=128)
    def get_logger(self, name: str):
        return logging.getLogger(name)

    def log_event(self, message: str, level: int = logging.INFO):
        self.logger.log(level, message)

_instance = PerformanceLogger()

def get_logger(name: str = "default"):
    return _instance.get_logger(name)

def log(message: str):
    _instance.log_event(message)