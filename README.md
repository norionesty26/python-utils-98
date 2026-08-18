# python-utils-98

A collection of Python utility functions designed to simplify everyday programming tasks. With a focus on common functionalities, this library helps streamline your workflow and improve code readability.

## Features

- **String Manipulation**: Effortlessly format, split, and sanitize strings with utility functions that handle common text processing tasks.
- **File Operations**: Simplify file reading, writing, and path management with easy-to-use methods that support both local and cloud storage.
- **Date and Time Utilities**: Work seamlessly with date and time objects, including formatting, parsing, and calculating time differences.
- **Data Validation**: Quickly validate inputs such as email addresses, phone numbers, and other common data types to ensure data integrity.

## Installation

To install the python-utils-98 package, you can use pip. Run the following command in your terminal:

```bash
pip install python-utils-98
```

## Basic Usage

Here’s a quick example demonstrating some of the capabilities of python-utils-98:

```python
from python_utils import StringUtils, FileUtils, DateUtils

# String manipulation
formatted_str = StringUtils.capitalize_words("hello world!")
print(formatted_str)  # Output: Hello World!

# File operations
FileUtils.write_file("example.txt", "This is a sample text.")
file_content = FileUtils.read_file("example.txt")
print(file_content)  # Output: This is a sample text.

# Date utilities
today = DateUtils.get_today()
print(today)  # Output: Current date in YYYY-MM-DD format

# Data validation
is_valid_email = StringUtils.validate_email("example@gmail.com")
print(is_valid_email)  # Output: True
```

## License

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.