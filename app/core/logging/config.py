"""
SecGenie.ai Logging Configuration
"""

import logging
import sys


def setup_logging() -> None:
    """
    Configure application logging.
    """

    logging.basicConfig(
        level=logging.INFO,
        format=(
            "%(asctime)s | "
            "%(levelname)s | "
            "%(name)s | "
            "%(message)s"
        ),
        handlers=[
            logging.StreamHandler(sys.stdout)
        ],
    )


def get_logger(name: str) -> logging.Logger:
    """
    Return application logger.
    """

    return logging.getLogger(name)