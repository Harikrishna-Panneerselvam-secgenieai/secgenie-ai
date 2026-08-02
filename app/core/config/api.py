from .base import BaseConfigModel


class APISettings(BaseConfigModel):
    """API configuration."""

    prefix: str = "/api/v1"

    version: str = "v1"

    docs_enabled: bool = True

    redoc_enabled: bool = True

    openapi_enabled: bool = True
