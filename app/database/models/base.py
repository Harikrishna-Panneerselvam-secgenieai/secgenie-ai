"""SQLAlchemy declarative base."""

from sqlalchemy.orm import DeclarativeBase

from app.database.models.mixins import (
    UUIDMixin,
    TimestampMixin,
    AuditMixin,
    SoftDeleteMixin,
)


class Base(
    UUIDMixin,
    TimestampMixin,
    AuditMixin,
    SoftDeleteMixin,
    DeclarativeBase,
):
    """
    Base class for all database models.
    """

    pass