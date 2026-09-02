# python-utils-98

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

python-utils-98 is a lightweight collection of general-purpose Python utilities for everyday development tasks. It provides reliable, dependency-free helpers that reduce boilerplate in file handling, data processing, and performance monitoring.

## Features

- Safe file operations with automatic directory creation and encoding detection
- Date and time utilities for parsing, formatting, and relative calculations
- Configuration loader that merges JSON, YAML, and environment variables
- Decorators for retry logic with exponential backoff and execution timing

## Installation

```bash
pip install python-utils-98
```

## Usage

```python
from python_utils_98 import read_file, load_config, Timer

# Read file with automatic directory handling
content = read_file("data/input.txt")

# Load merged configuration
config = load_config("config.json", env_prefix="APP_")

# Measure execution time
with Timer() as t:
    result = process_data()
print(f"Done in {t.elapsed:.2f}s")
```

## License

Released under the MIT License.