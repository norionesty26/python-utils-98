import os
from typing import Final

# Application configuration constants
APP_NAME: Final[str] = "python-utils-98"
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3

# Directory and path defaults
BASE_DIR: Final[str] = os.path.dirname(os.path.abspath(__file__))
LOG_DIR: Final[str] = os.path.join(BASE_DIR, "logs")
TEMP_DIR: Final[str] = os.path.join(BASE_DIR, "temp")

# Content type and encoding definitions
UTF_8: Final[str] = "utf-8"
JSON_CONTENT_TYPE: Final[str] = "application/json"

# Validation constraints
MIN_PASSWORD_LENGTH: Final[int] = 12
ALLOWED_EXTENSIONS: Final[set[str]] = {".txt", ".csv", ".json", ".log"}

def get_environment_config() -> dict[str, str]:
    return {
        "env": os.getenv("APP_ENV", "development"),
        "debug": os.getenv("APP_DEBUG", "false"),
    }