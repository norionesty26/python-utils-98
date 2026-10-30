import os
from typing import Final

# Application paths
BASE_DIR: Final[str] = os.path.dirname(os.path.abspath(__file__))
LOG_DIR: Final[str] = os.path.join(BASE_DIR, 'logs')

# Environment defaults
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3

# Supported formats
SUPPORTED_EXTENSIONS: Final[tuple[str, ...]] = ('.json', '.yaml', '.yml')

# Error messages
ERR_INVALID_CONFIG: Final[str] = 'invalid configuration format provided'
ERR_TIMEOUT_REACHED: Final[str] = 'operation timed out'

class ConfigKeys:
    DB_HOST: Final[str] = 'DB_HOST'
    DB_PORT: Final[str] = 'DB_PORT'
    API_KEY: Final[str] = 'API_KEY'

# Internal constraints
MAX_BUFFER_SIZE: Final[int] = 1024 * 1024