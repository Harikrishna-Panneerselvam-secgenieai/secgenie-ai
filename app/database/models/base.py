"""SQLAlchemy declarative base for all ORM models."""

from sqlalchemy.orm import DeclarativeBase

from app.database.models.mixins import (
    AuditMixin,
    SoftDeleteMixin,
    TimestampMixin,
    UUIDMixin,
)


class Base(
    UUIDMixin,
    TimestampMixin,
    AuditMixin,
    SoftDeleteMixin,
    DeclarativeBase,
):
    """
    Base class for all SQLAlchemy ORM models.

    Provides:
    - UUID primary key
    - Created/updated timestamps
    - Audit fields
    - Soft delete functionality
    """

    pass