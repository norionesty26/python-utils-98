# python-utils-98

A robust collection of high-performance utility functions designed to streamline daily Python development tasks. This library simplifies complex boilerplate code into efficient, clean, and reusable components.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features

*   **File System Helpers:** Simplified recursive directory searching and file type filtering with built-in error handling.
*   **Performance Decorators:** Ready-to-use `@timer` and `@retry` decorators to track execution time and handle transient network failures gracefully.
*   **Data Validation:** Lightweight schemas for validating configuration dictionaries and environment variables without heavy dependencies.
*   **String Sanitization:** Optimized regex patterns for cleaning input, stripping whitespace, and normalizing file paths across different operating systems.

## Installation

Install the package via pip:

```bash
pip install python-utils-98
```

Alternatively, if you are working within a virtual environment, ensure your dependencies are updated:

```bash
pip install --upgrade python-utils-98
```

## Basic Usage

Import specific modules to handle routine tasks efficiently. The following example demonstrates using the timer decorator to profile a function:

```python
from python_utils_98.decorators import timer
from python_utils_98.files import list_files

# Use the timer to profile execution
@timer
def process_data():
    files = list_files("./data", extension=".json")
    return len(files)

count = process_data()
print(f"Processed {count} files.")
```

## Requirements

*   Python 3.8+
*   No external dependencies; written in pure Python.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.