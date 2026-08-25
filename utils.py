from typing import Any, Dict, List, Optional, Union
def safe_divide(a: Union[int, float], b: Union[int, float]) -> Optional[float]:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def safe_int_parse(value: Any) -> Optional[int]:
    if value is None:
        raise ValueError("Cannot parse None")
    if isinstance(value, (int, float)):
        return int(value)
    if isinstance(value, str):
        stripped = value.strip()
        if not stripped:
            raise ValueError("Empty string cannot be parsed to int")
        try:
            return int(stripped)
        except ValueError:
            raise ValueError(f"Invalid integer format: {value}") from None
    raise TypeError("Unsupported type for integer parsing")

def safe_index(lst: List[Any], index: int, default: Any = None) -> Any:
    if not isinstance(lst, list):
        raise TypeError("First argument must be a list")
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    if index < 0 or index >= len(lst):
        return default
    return lst[index]

def safe_get(d: Dict[str, Any], key: str, default: Any = None) -> Any:
    if not isinstance(d, dict):
        raise TypeError("First argument must be a dictionary")
    if not isinstance(key, str):
        raise TypeError("Key must be a string")
    return d.get(key, default)

def process_numbers(numbers: List[Union[int, float]]) -> float:
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if len(numbers) == 0:
        raise ValueError("Cannot process empty list")
    total = 0.0
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError("All elements must be numbers")
        total += num
    return total / len(numbers)