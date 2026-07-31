"""Base model for all SQLAlchemy ORM models."""

from __future__ import annotations

from app.database.base import Base
from app.models.mixins import (
    AuditMixin,
    SoftDeleteMixin,
    TimestampMixin,
    UUIDPrimaryKeyMixin,
)


class BaseModel(
    UUIDPrimaryKeyMixin,
    TimestampMixin,
    AuditMixin,
    SoftDeleteMixin,
    Base,
):
    """
    Abstract base model for all ORM entities.

    Provides:
    - UUID primary key
    - Created/updated timestamps
    - Created/updated by
    - Soft delete support
    """

    __abstract__ = True