from app.core.logging.config import get_logger, setup_logging

setup_logging()

logger = get_logger(__name__)

logger.info("Application started")

try:
    _ = 1 / 0
except ZeroDivisionError:
    logger.exception("Unexpected exception")