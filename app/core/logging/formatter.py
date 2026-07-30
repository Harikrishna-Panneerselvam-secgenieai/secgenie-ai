"""
JSON formatter for structured application logging.

This formatter converts Python LogRecord objects into a standardized
JSON representation as defined in docs/standards/logging_schema.md.
"""

from __future__ import annotations

import json
import logging
from datetime import UTC, datetime
from typing import Any

from app.core.logging.context import (
    get_correlation_id,
    get_execution_id,
    get_request_id,
)


class JsonFormatter(logging.Formatter):
    """
    Formats log records as compact JSON.
    """

    # Standard LogRecord attributes that should not be duplicated.
    RESERVED_FIELDS = {
        "name",
        "msg",
        "args",
        "levelname",
        "levelno",
        "pathname",
        "filename",
        "module",
        "exc_info",
        "exc_text",
        "stack_info",
        "lineno",
        "funcName",
        "created",
        "msecs",
        "relativeCreated",
        "thread",
        "threadName",
        "processName",
        "process",
        "message",
        "taskName",
    }

    def format(self, record: logging.LogRecord) -> str:
        """
        Convert a LogRecord into a JSON string.
        """

        log_record: dict[str, Any] = {
            "timestamp": datetime.fromtimestamp(
                record.created,
                tz=UTC,
            ).isoformat(timespec="milliseconds").replace("+00:00", "Z"),
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name,
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
            "request_id": get_request_id(),
            "correlation_id": get_correlation_id(),
            "execution_id": get_execution_id(),
        }

        # Include custom fields passed through logger(..., extra={...}).
        for key, value in record.__dict__.items():
            if key not in self.RESERVED_FIELDS and key not in log_record:
                log_record[key] = value

        # Include exception information when available.
        if record.exc_info:
            log_record["exception"] = self.formatException(record.exc_info)

        return json.dumps(
            log_record,
            ensure_ascii=False,
            separators=(",", ":"),
        )