from .base import BaseConfigModel


class DatabaseSettings(BaseConfigModel):
    """Database configuration."""

    host: str = "localhost"
    port: int = 5432

    username: str = "postgres"
    password: str = ""

    database: str = "secgenie"

    echo: bool = False

    pool_size: int = 10
    max_overflow: int = 20

    pool_timeout: int = 30
    pool_recycle: int = 1800