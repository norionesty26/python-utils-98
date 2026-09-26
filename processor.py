from dataclasses import dataclass, field
from typing import Any, Callable, List


@dataclass
class ProcessingResult:
    success: bool
    data: Any
    errors: List[str] = field(default_factory=list)


class DataProcessor:
    def __init__(self) -> None:
        self._pipeline: List[Callable[[Any], Any]] = []

    def add_step(self, func: Callable[[Any], Any]) -> "DataProcessor":
        self._pipeline.append(func)
        return self

    def clear_pipeline(self) -> None:
        self._pipeline.clear()

    def process(self, data: Any) -> ProcessingResult:
        current_data = data
        errors: List[str] = []

        for index, step in enumerate(self._pipeline):
            try:
                current_data = step(current_data)
            except Exception as err:
                step_name = getattr(step, "__name__", str(step))
                errors.append(f"Step {index} ({step_name}) failed: {err}")
                return ProcessingResult(success=False, data=None, errors=errors)

        return ProcessingResult(success=True, data=current_data, errors=[])

    def process_batch(self, items: List[Any]) -> List[ProcessingResult]:
        return [self.process(item) for item in items]
