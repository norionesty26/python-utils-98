import os
from typing import Final

# Environment configuration constants
ENV_PREFIX: Final[str] = "PY_UTILS_"
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3

# Path constants
BASE_DIR: Final[str] = os.path.dirname(os.path.abspath(__file__))
LOG_DIR: Final[str] = os.path.join(BASE_DIR, "logs")
TEMP_DIR: Final[str] = os.path.join(BASE_DIR, "temp")

# Resource limits
CHUNK_SIZE: Final[int] = 8192
BUFFER_SIZE: Final[int] = 1024 * 1024

# Validation patterns
EMAIL_REGEX: Final[str] = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
UUID_REGEX: Final[str] = r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"

# Supported formats
SUPPORTED_EXTENSIONS: Final[set[str]] = {".json", ".yaml", ".csv", ".txt"}

def get_timeout() -> int:
    return int(os.getenv(f"{ENV_PREFIX}TIMEOUT", DEFAULT_TIMEOUT))