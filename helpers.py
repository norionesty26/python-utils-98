import math
from datetime import datetime, timezone
from typing import Any, Generator, Iterable, TypeVar

T = TypeVar("T")


def chunk_iterable(iterable: Iterable[T], chunk_size: int) -> Generator[list[T], None, None]:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero")
    chunk: list[T] = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == chunk_size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def deep_get(data: dict[str, Any], keys: str, default: Any = None) -> Any:
    current = data
    for key in keys.split("."):
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current


def truncate_text(text: str, max_length: int, suffix: str = "...") -> str:
    if max_length <= len(suffix):
        raise ValueError(f"max_length must be greater than suffix length ({len(suffix)})")
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)] + suffix


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()
