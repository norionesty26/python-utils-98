from typing import Final

# Application configuration constants
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3
CHUNK_SIZE: Final[int] = 4096

# System path patterns
LOG_DIR: Final[str] = "/var/log/python-utils-98"
TEMP_DIR: Final[str] = "/tmp/python-utils-98"

# Encoding and validation constants
ENCODING: Final[str] = "utf-8"
SUPPORTED_EXTENSIONS: Final[tuple[str, ...]] = (".json", ".yaml", ".toml")

# Environment keys
ENV_PREFIX: Final[str] = "PU98"

class ExitCodes:
    SUCCESS: int = 0
    ERROR_GENERAL: int = 1
    ERROR_CONFIG: int = 2
    ERROR_IO: int = 3