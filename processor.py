import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)

def validate_payload(data: Any) -> bool:
    if not isinstance(data, dict):
        return False
    required_keys = {'id', 'value', 'timestamp'}
    return all(k in data for k in required_keys)

def process_stream(data_stream: list[Dict[str, Any]]) -> None:
    for entry in data_stream:
        if not validate_payload(entry):
            logger.warning(f"Skipping invalid payload: {entry}")
            continue
        
        try:
            result = entry['value'] * 2
            logger.info(f"Processed {entry['id']}: {result}")
        except (TypeError, KeyError) as e:
            logger.error(f"Processing error for {entry.get('id')}: {e}")

if __name__ == "__main__":
    sample_data = [
        {'id': 1, 'value': 10, 'timestamp': 1625097600},
        {'invalid': 'data'},
        {'id': 2, 'value': 20, 'timestamp': 1625097601}
    ]
    process_stream(sample_data)