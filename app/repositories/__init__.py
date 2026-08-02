"""
Repository layer.

Repositories encapsulate all database access logic and provide
a clean interface between the Service layer and SQLAlchemy.

All repositories should inherit from BaseRepository.
"""

from app.repositories.base import BaseRepository

__all__ = ["BaseRepository"]
