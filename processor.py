import logging
from typing import Any, Dict

def validate_payload(data: Any) -> bool:
    if not isinstance(data, dict):
        return False
    return all(key in data for key in ('id', 'value'))

def process_data(batch: list) -> None:
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    for entry in batch:
        try:
            if not validate_payload(entry):
                logger.warning(f"Invalid entry skipped: {entry}")
                continue
            
            result = entry['value'] * 2
            logger.info(f"Processed {entry['id']}: {result}")
        except (KeyError, TypeError, ValueError) as e:
            logger.error(f"Processing error: {e}")
            continue

if __name__ == "__main__":
    test_data = [
        {'id': 1, 'value': 10},
        {'id': 2, 'value': 'invalid'},
        {'invalid': 'data'},
        {'id': 3, 'value': 25}
    ]
    process_data(test_data)