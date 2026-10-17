# python-utils-98

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

`python-utils-98` is a lightweight, zero-dependency Python library designed to streamline common data transformation, file handling, and string manipulation tasks. It provides a cohesive collection of battle-tested helper functions to reduce boilerplate code across modern Python applications.

## Features

* **Smart Dictionary Merging**: Perform deep merges on nested dictionaries with configurable collision handling.
* **Safe File Operations**: Write files atomically to prevent partial writes, with automated directory creation and SHA-256 checksum validation.
* **String Case Transformer**: Convert text effortlessly between `camelCase`, `snake_case`, `PascalCase`, and `kebab-case`.
* **Execution Profiling**: Measure block execution time with microsecond accuracy using lightweight context managers and decorators.

## Installation

Install the package via `pip`:

```bash
pip install python-utils-98
```

Alternatively, install directly from source:

```bash
git clone https://github.com/Developer/python-utils-98.git
cd python-utils-98
pip install .
```

## Quick Start

Here is a quick example showing dictionary merging and string formatting in action:

```python
from python_utils_98 import deep_merge, to_snake_case, SafeWriter

# Deep merge nested dictionaries
base_config = {"db": {"host": "localhost", "port": 5432}}
override_config = {"db": {"port": 5433, "user": "admin"}}

final_config = deep_merge(base_config, override_config)
print(final_config)
# Output: {'db': {'host': 'localhost', 'port': 5433, 'user': 'admin'}}

# Normalize object keys
raw_key = "userProfileSettings"
clean_key = to_snake_case(raw_key)
print(clean_key)
# Output: 'user_profile_settings'

# Safe atomic file write
with SafeWriter("config.json") as writer:
    writer.write('{"status": "ok"}')
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.