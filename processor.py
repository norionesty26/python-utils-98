from typing import Any, Callable, Dict, List, Optional


class ProcessingError(Exception):
    pass


class BatchProcessor:
    def __init__(self, fail_fast: bool = False) -> None:
        self.fail_fast = fail_fast
        self.errors: List[Dict[str, Any]] = []

    def process_item(
        self, item: Any, transform: Callable[[Any], Any]
    ) -> Optional[Any]:
        if item is None:
            return None
        try:
            return transform(item)
        except (ValueError, TypeError, ZeroDivisionError, KeyError) as err:
            error_info = {
                "item": item,
                "error": str(err),
                "type": type(err).__name__,
            }
            self.errors.append(error_info)
            if self.fail_fast:
                raise ProcessingError(f"Failed processing item: {err}") from err
            return None

    def process_batch(
        self, items: List[Any], transform: Callable[[Any], Any]
    ) -> List[Any]:
        if not isinstance(items, list):
            raise TypeError(f"Expected list, got {type(items).__name__}")

        results = []
        for item in items:
            res = self.process_item(item, transform)
            if res is not None:
                results.append(res)
        return results

    def clear_errors(self) -> None:
        self.errors.clear()
