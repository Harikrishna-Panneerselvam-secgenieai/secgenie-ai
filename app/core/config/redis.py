from .base import BaseConfigModel


class RedisSettings(BaseConfigModel):
    """Redis configuration."""

    host: str = "localhost"
    port: int = 6379

    password: str = ""

    db: int = 0

    ssl: bool = False
