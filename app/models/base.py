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
    """

    __abstract__ = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        if getattr(self, "is_deleted", None) is None:
            self.is_deleted = False