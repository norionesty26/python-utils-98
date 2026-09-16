from typing import Final, Any, Dict, List, Union

# Data handling constants
DEFAULT_ENCODING: Final[str] = "utf-8"
MAX_RETRY_ATTEMPTS: Final[int] = 3
TIMEOUT_SECONDS: Final[float] = 30.0

# Type alias definitions for common data structures
DataPayload = Dict[str, Any]
DataList = List[DataPayload]
Primitive = Union[str, int, float, bool, None]

HTTP_SUCCESS_CODES: Final[set[int]] = {200, 201, 204}

RESERVED_KEYS: Final[List[str]] = [
    "id",
    "metadata",
    "timestamp",
    "created_at",
    "updated_at"
]

# Validation constraints
MIN_BATCH_SIZE: Final[int] = 1
MAX_BATCH_SIZE: Final[int] = 1000

def get_default_config() -> DataPayload:
    return {
        "encoding": DEFAULT_ENCODING,
        "retries": MAX_RETRY_ATTEMPTS,
        "timeout": TIMEOUT_SECONDS,
        "reserved": RESERVED_KEYS
    }