import time
from collections import OrderedDict
from functools import wraps
from itertools import islice
from typing import Callable, Any, Generator, Iterable

def ttl_cache(maxsize: int = 128, ttl: float = 60.0) -> Callable:
    def decorator(func: Callable) -> Callable:
        cache: OrderedDict = OrderedDict()

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            key = (args, tuple(sorted(kwargs.items()))) if kwargs else args
            now = time.monotonic()

            if key in cache:
                val, expiry = cache[key]
                if now < expiry:
                    cache.move_to_end(key)
                    return val
                del cache[key]

            result = func(*args, **kwargs)
            if len(cache) >= maxsize:
                cache.popitem(last=False)
            cache[key] = (result, now + ttl)
            return result

        wrapper.cache_clear = cache.clear  # type: ignore
        return wrapper
    return decorator

def chunked(iterable: Iterable, size: int) -> Generator[list, None, None]:
    it = iter(iterable)
    while True:
        chunk = list(islice(it, size))
        if not chunk:
            return
        yield chunk