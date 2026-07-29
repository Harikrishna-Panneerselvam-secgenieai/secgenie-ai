"""                FastAPI Router
                     |
                     |
              dependencies.py
                     |
        +------------+-------------+
        |            |             |
   Database      Repository     Services
    Session          |             |
        |            |             |
    PostgreSQL   SQLAlchemy    Business Logic
                     
                     |
                     |
               AI Providers
                     |
        +------------+------------+
        |                         |
      OpenAI                   Claude
      Local LLM                Azure OpenAI"""


from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.database.session import async_session_factory


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Provide a database session for each request.
    """
    async with async_session_factory() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise


def get_settings():
    """
    Return the application settings singleton.
    """
    return settings