import logging
import sys
from typing import Any, Dict, Optional


class StructuredLogger:
    def __init__(self, name: str = "app", level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        if not self.logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter(
                "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def _format_extra(self, extra: Optional[Dict[str, Any]] = None) -> str:
        if not extra:
            return ""
        return " | " + " ".join(f"{k}={v}" for k, v in extra.items())

    def info(self, msg: str, extra: Optional[Dict[str, Any]] = None) -> None:
        self.logger.info(f"{msg}{self._format_extra(extra)}")

    def error(self, msg: str, extra: Optional[Dict[str, Any]] = None) -> None:
        self.logger.error(f"{msg}{self._format_extra(extra)}")

    def warning(self, msg: str, extra: Optional[Dict[str, Any]] = None) -> None:
        self.logger.warning(f"{msg}{self._format_extra(extra)}")

    def debug(self, msg: str, extra: Optional[Dict[str, Any]] = None) -> None:
        self.logger.debug(f"{msg}{self._format_extra(extra)}")


def get_logger(name: str = "app") -> StructuredLogger:
    return StructuredLogger(name)
