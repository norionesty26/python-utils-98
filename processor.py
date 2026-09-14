import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

class ProcessingError(Exception):
    pass

def safe_process(data: Any) -> Optional[Any]:
    try:
        if data is None:
            raise ValueError("input data cannot be null")
        
        if not isinstance(data, (dict, list)):
            raise TypeError(f"unsupported data type: {type(data).__name__}")

        return _internal_transform(data)

    except (ValueError, TypeError) as e:
        logger.error(f"validation error: {e}")
        return None
    except Exception as e:
        logger.exception(f"unexpected processing failure: {e}")
        raise ProcessingError("critical failure during transformation") from e

def _internal_transform(data: Any) -> Any:
    if isinstance(data, dict):
        return {str(k): v for k, v in data.items()}
    return [item for item in data if item is not None]

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    print(safe_process({"key": "value"}))