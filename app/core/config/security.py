from pydantic import Field

from .base import BaseConfigModel


class SecuritySettings(BaseConfigModel):
    """Application security configuration."""

    allowed_hosts: list[str] = Field(default_factory=lambda: ["*"])

    cors_origins: list[str] = Field(default_factory=lambda: ["*"])

    trusted_proxies: list[str] = Field(default_factory=list)


class JWTSettings(BaseConfigModel):
    """JWT authentication configuration."""

    secret_key: str = ""

    algorithm: str = "HS256"

    access_token_expire_minutes: int = 30

    refresh_token_expire_days: int = 7