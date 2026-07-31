"""
Soft Delete Mixin

Provides logical deletion functionality for SQLAlchemy models.

Instead of permanently removing records from the database,
records are marked as deleted by setting the deleted_at timestamp.

Features:
- Soft delete
- Restore
- Deletion status property
- Idempotent operations (safe to call multiple times)
"""

from __future__ import annotations

from datetime import UTC, datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column


class SoftDeleteMixin:
    """
    Reusable mixin providing soft delete functionality.

    Models inheriting this mixin gain:

    - deleted_at timestamp
    - soft_delete()
    - restore()
    - is_deleted property
    """

    deleted_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        default=None,
        index=True,
        doc="Timestamp when the record was soft deleted.",
    )

    @property
    def is_deleted(self) -> bool:
        """
        Return True if the record has been soft deleted.

        Returns:
            bool: True if deleted, otherwise False.
        """
        return self.deleted_at is not None

    def soft_delete(self) -> None:
        """
        Mark the record as deleted.

        This method is idempotent. Calling it multiple times
        will preserve the original deletion timestamp.
        """
        if self.deleted_at is None:
            self.deleted_at = datetime.now(UTC)

    def restore(self) -> None:
        """
        Restore a previously soft-deleted record.

        This method is idempotent.
        """
        self.deleted_at = None