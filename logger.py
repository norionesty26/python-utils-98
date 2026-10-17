import logging
from functools import lru_cache

class PerformanceLogger:
    def __init__(self, name: str = 'python-utils-98') -> None:
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    @lru_cache(maxsize=128)
    def get_formatted_message(self, message: str) -> str:
        return f'[{self.logger.name}] {message}'

    def info(self, message: str) -> None:
        self.logger.info(self.get_formatted_message(message))

    def error(self, message: str) -> None:
        self.logger.error(self.get_formatted_message(message))

def get_logger(name: str = 'python-utils-98') -> PerformanceLogger:
    return PerformanceLogger(name)