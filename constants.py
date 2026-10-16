import os
from typing import Final

# Application configuration constants
APP_NAME: Final[str] = "python-utils-98"
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3

# Environment configuration
ENV: Final[str] = os.getenv("APP_ENV", "production")
DEBUG: Final[bool] = os.getenv("DEBUG", "false").lower() == "true"

# Path definitions
BASE_DIR: Final[str] = os.path.dirname(os.path.abspath(__file__))
LOG_DIR: Final[str] = os.path.join(BASE_DIR, "logs")

# Default headers
DEFAULT_HEADERS: Final[dict[str, str]] = {
    "Content-Type": "application/json",
    "User-Agent": f"{APP_NAME}/1.0"
}

# Validation constraints
MIN_PASSWORD_LENGTH: Final[int] = 12
ALLOWED_EXTENSIONS: Final[set[str]] = {".json", ".csv", ".yaml"}

# Error messages
ERR_TIMEOUT: Final[str] = "operation timed out"
ERR_AUTH: Final[str] = "authentication failed"
