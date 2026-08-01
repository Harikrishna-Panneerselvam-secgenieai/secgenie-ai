"""Database engine and session configuration."""

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.core.config.settings import settings

DATABASE_URL = (
    f"postgresql+asyncpg://"
    f"{settings.database.username}:"
    f"{settings.database.password}@"
    f"{settings.database.host}:"
    f"{settings.database.port}/"
    f"{settings.database.database}"
)

engine: AsyncEngine = create_async_engine(
    DATABASE_URL,
    echo=settings.database.echo,
    pool_size=settings.database.pool_size,
    max_overflow=settings.database.max_overflow,
    pool_timeout=settings.database.pool_timeout,
    pool_recycle=settings.database.pool_recycle,
)

async_session_factory = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=False,
    expire_on_commit=False,
)