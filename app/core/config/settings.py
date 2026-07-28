from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Application
    app_name: str = "SecGenie AI"
    app_version: str = "0.1.0"
    app_env: str = "development"
    debug: bool = False

    # Server
    host: str = "127.0.0.1"
    port: int = 8000

    # Database
    database_url: str = ""

    # Redis
    redis_url: str = ""

    # JWT
    jwt_secret_key: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """Return a cached Settings instance."""
    return Settings()


settings = get_settings()