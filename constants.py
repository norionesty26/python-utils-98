import os
from typing import Final

# Application configuration constants
APP_NAME: Final[str] = "python-utils-98"
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3

# Path settings
BASE_DIR: Final[str] = os.path.dirname(os.path.abspath(__file__))
LOG_DIR: Final[str] = os.path.join(BASE_DIR, "logs")

# Environment defaults
ENV_PREFIX: Final[str] = "PY_UTILS_"
DEBUG_MODE: Final[bool] = os.getenv(f"{ENV_PREFIX}DEBUG", "False").lower() == "true"

# Validation constraints
MIN_PASSWORD_LENGTH: Final[int] = 12
SUPPORTED_EXTENSIONS: Final[tuple[str, ...]] = (".py", ".json", ".yaml")

class ExitCodes:
    SUCCESS: Final[int] = 0
    ERROR_GENERAL: Final[int] = 1
    ERROR_INVALID_INPUT: Final[int] = 2
    ERROR_CONNECTION: Final[int] = 3