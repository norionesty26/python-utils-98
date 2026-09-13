# python-utils-98

A robust collection of high-performance Python utilities designed to streamline common data processing and system automation tasks. This library focuses on efficiency, type safety, and minimal dependencies for seamless integration into any production environment.

## Features

*   **Robust File I/O:** Simplified wrappers for handling recursive directory traversal, thread-safe logging, and automated cleanup of temporary storage.
*   **Data Validation:** A lightweight set of decorators for enforcing schema constraints and data type integrity across complex JSON payloads.
*   **Concurrent Execution:** Easy-to-implement task queuing and parallel execution primitives built on `concurrent.futures`.
*   **Cross-Platform Pathing:** Unified path manipulation utilities that handle OS-specific path separators without extra configuration.

## Installation

Install the package via `pip` from PyPI:

```bash
pip install python-utils-98
```

Alternatively, install from source for the latest development features:

```bash
git clone https://github.com/Developer/python-utils-98.git
cd python-utils-98
pip install .
```

## Basic Usage

The library is designed with a clean API, allowing you to import specific utilities as needed:

```python
from pyutils98.file_ops import SafeFileWriter
from pyutils98.validators import validate_schema

# Initialize a protected file writer
writer = SafeFileWriter('output.log')
writer.append("Process initialized successfully.")

# Validate incoming data structures
data = {"id": 1, "status": "active"}
if validate_schema(data, {"id": int, "status": str}):
    print("Payload integrity verified.")
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.