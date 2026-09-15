from typing import List, Optional, Any, Callable

class DataProcessor:
    """Utility class for systematic data transformation."""

    def __init__(self, transform_func: Optional[Callable[[Any], Any]] = None) -> None:
        self.transform_func = transform_func

    def process_batch(self, items: List[Any]) -> List[Any]:
        """Apply transformation function to a list of items."""
        if not self.transform_func:
            return items
        return [self.transform_func(item) for item in items]

    @staticmethod
    def flatten(nested_list: List[List[Any]]) -> List[Any]:
        """Flatten a list of lists into a single list."""
        return [item for sublist in nested_list for item in sublist]

    def filter_none(self, items: List[Optional[Any]]) -> List[Any]:
        """Remove all None values from a list."""
        return [item for item in items if item is not None]

def create_processor(func: Optional[Callable[[Any], Any]] = None) -> DataProcessor:
    """Factory function for DataProcessor instances."""
    return DataProcessor(transform_func=func)