import logging
from typing import Any, List

logging.basicConfig(level=logging.INFO)

def process_items(data: List[Any]) -> None:
    if not isinstance(data, list):
        raise ValueError('input must be a list')

    for item in data:
        if not isinstance(item, (int, float)):
            logging.warning(f'skipping invalid item: {item}')
            continue

        result = item * 2
        logging.info(f'processed {item} to {result}')

def main():
    sample_data = [1, 'invalid', 3.5, None, 10]
    try:
        process_items(sample_data)
    except ValueError as e:
        logging.error(f'processing failed: {e}')

if __name__ == '__main__':
    main()