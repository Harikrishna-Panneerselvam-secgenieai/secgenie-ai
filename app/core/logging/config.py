"""
SecGenie.ai Logging Configuration
"""

from __future__ import annotations

import logging
import sys

from app.core.logging.formatter import JsonFormatter


def setup_logging() -> None:
    """
    Configure application-wide structured logging.
    """

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # Remove existing handlers to avoid duplicate logs
    root_logger.handlers.clear()

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JsonFormatter())

    root_logger.addHandler(handler)


def get_logger(name: str) -> logging.Logger:
    """
    Return an application logger.

    Args:
        name: Logger name (typically __name__)

    Returns:
        Configured logger instance.
    """
    return logging.getLogger(name)
