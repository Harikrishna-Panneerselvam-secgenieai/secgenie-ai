from .base import BaseConfigModel


class LoggingSettings(BaseConfigModel):
    """Logging configuration."""

    level: str = "INFO"

    format: str = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

    file: str = "logs/secgenie.log"
