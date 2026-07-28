from .base import BaseConfigModel


class AppSettings(BaseConfigModel):
    """Application configuration."""

    app_name: str = "SecGenie AI"
    app_version: str = "0.1.0"

    environment: str = "development"

    debug: bool = False