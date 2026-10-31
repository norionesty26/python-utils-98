import logging
from typing import Any, Dict, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_input(data: Any) -> bool:
    return isinstance(data, dict) and 'id' in data and isinstance(data['id'], int)

def process_item(item: Dict[str, Any]) -> None:
    logger.info(f"Processing item: {item.get('id')}")

def run_processing_loop(items: list) -> None:
    for item in items:
        try:
            if not validate_input(item):
                logger.warning(f"Invalid input skipped: {item}")
                continue
            process_item(item)
        except Exception as e:
            logger.error(f"Unexpected processing error: {e}")

if __name__ == '__main__':
    data_stream = [{'id': 1}, {'id': 'invalid'}, {'id': 2}, None]
    run_processing_loop(data_stream)