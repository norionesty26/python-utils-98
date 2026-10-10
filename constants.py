from typing import Final, Any, Dict

# Data handling thresholds and constraints
DEFAULT_CHUNK_SIZE: Final[int] = 1024
MAX_RETRY_ATTEMPTS: Final[int] = 3
TIMEOUT_SECONDS: Final[float] = 30.0

# Default data mappings
EMPTY_MAP: Final[Dict[Any, Any]] = {}
SUPPORTED_ENCODINGS: Final[tuple] = ('utf-8', 'ascii', 'latin-1')

# Error and status messages
ERROR_MSG_INVALID_INPUT: Final[str] = 'Invalid data input format provided'
ERROR_MSG_TIMEOUT: Final[str] = 'Operation timed out during execution'

class DataConstants:
    """Namespace for application-wide configuration constants."""
    @classmethod
    def get_supported_encodings(cls) -> tuple:
        return SUPPORTED_ENCODINGS

    @classmethod
    def get_max_retries(cls) -> int:
        return MAX_RETRY_ATTEMPTS