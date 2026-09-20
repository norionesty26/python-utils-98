from typing import Dict, Any, Generator, Iterable, TypeVar, List

T = TypeVar('T')

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flatten a nested dictionary.

    Args:
        d: The dictionary to flatten.
        parent_key: The prefix to prepend to keys.
        sep: The separator between nested keys.

    Returns:
        A flattened dictionary.
    """
    items: List[tuple] = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def chunk_iterable(iterable: Iterable[T], size: int) -> Generator[List[T], None, None]:
    """Yield successive n-sized chunks from an iterable.

    Args:
        iterable: The iterable collection to chunk.
        size: The size of each chunk.

    Yields:
        A generator yielding chunks as lists.
    """
    iterator = iter(iterable)
    while True:
        chunk: List[T] = []
        for _ in range(size):
            try:
                chunk.append(next(iterator))
            except StopIteration:
                if chunk:
                    yield chunk
                return
        yield chunk
