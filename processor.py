from typing import Any, List, Optional

class DataProcessor:
    """Processor for handling data transformations and filtering."""

    def __init__(self, items: Optional[List[Any]] = None) -> None:
        self.items = items or []

    def add_item(self, item: Any) -> None:
        """Append a single item to the internal collection."""
        self.items.append(item)

    def filter_by_type(self, data_type: type) -> List[Any]:
        """Return list containing only items of specified type."""
        return [item for item in self.items if isinstance(item, data_type)]

    def get_summary(self) -> dict:
        """Return a mapping of types to their counts."""
        summary: dict[str, int] = {}
        for item in self.items:
            t_name = type(item).__name__
            summary[t_name] = summary.get(t_name, 0) + 1
        return summary

    def clear(self) -> None:
        """Empty the internal collection."""
        self.items.clear()

    def __repr__(self) -> str:
        """String representation of the processor state."""
        return f"DataProcessor(count={len(self.items)})"