# python-utils-98

A robust collection of high-performance Python utilities designed to streamline common programming tasks. This library focuses on providing clean, thread-safe, and dependency-minimal tools for daily development workflows.

## Features

*   **Robust File Operations:** Advanced context managers for safe file handling and automated cleanup of temporary directory structures.
*   **Time-Series Decorators:** Lightweight `@timer` and `@retry` decorators to monitor execution latency and improve task resilience.
*   **Type-Safe Collections:** Enhanced dictionary and list extensions that provide seamless data transformation and deep-merge capabilities.
*   **Logging Helpers:** Pre-configured logging wrappers that ensure consistent formatting across distributed development environments.

## Installation

Install `python-utils-98` directly from PyPI using pip:

```bash
pip install python-utils-98
```

Alternatively, for local development:

```bash
git clone https://github.com/Developer/python-utils-98.git
cd python-utils-98
pip install -e .
```

## Basic Usage

Utilize the performance monitoring decorators to track function execution times in your existing scripts:

```python
from python_utils_98.decorators import timer

@timer
def process_data(data_points):
    # Simulate heavy lifting
    return sum(data_points)

result = process_data([i for i in range(1000000)])
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.