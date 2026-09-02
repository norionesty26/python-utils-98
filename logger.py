import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = 'root', log_file: str = 'app.log', level: int = logging.INFO, max_bytes: int = 10485760, backup_count: int = 5) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    if not logger.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        dir_path = os.path.dirname(log_file)
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path)
        file_handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger

if __name__ == '__main__':
    logger = setup_logger('myapp')
    logger.info('Application started')
    for i in range(50):
        logger.info('Processing item %d', i)