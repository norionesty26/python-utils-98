# python-utils-98

A collection of lightweight, high-performance Python utilities designed to streamline daily automation and data processing tasks. This toolkit eliminates boilerplate code by providing robust wrappers for common file operations, logging, and concurrency management.

## Features

*   **FileStream API:** Simplified context managers for handling large file I/O operations without memory overflows.
*   **Safe-Thread Executor:** A clean wrapper around `concurrent.futures` with built-in exception handling and result logging.
*   **Config Loader:** A unified interface to load, parse, and validate environment variables and JSON/YAML configuration files.
*   **Time-it Decorator:** A decorator suite for precision profiling and benchmarking of individual functions or class methods.

## Installation

Install the package directly from PyPI:

```bash
pip install python-utils-98
```

For development mode, clone the repository and install dependencies:

```bash
git clone https://github.com/Developer/python-utils-98.git
cd python-utils-98
pip install -r requirements.txt
```

## Usage

Easily profile your code or manage file operations with minimal setup:

```python
from pyutils98 import timer, FileStream

# Benchmark any function with a single decorator
@timer
def heavy_computation():
    return sum(i * i for i in range(1000000))

# Safe file writing without manual closing
with FileStream("data.txt", mode="w") as f:
    f.write("System log entry")
```

## Contributing

Contributions are welcome! Please open an issue to discuss proposed changes or submit a pull request with unit tests covering your new functionality.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.