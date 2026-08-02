"""Database session dependency."""

from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session.database import async_session_factory


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Create and provide a database session.

    The session is automatically closed after use.
    """
    async with async_session_factory() as session:
        yield session
