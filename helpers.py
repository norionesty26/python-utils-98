import time
import functools

def retry(
    max_attempts=5,
    delay=1.0,
    backoff=2.0,
    exceptions=(Exception,)
):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    if attempt == max_attempts - 1:
                        raise
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator