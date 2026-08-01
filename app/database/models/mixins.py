"""Reusable SQLAlchemy model mixins."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime
from uuid import UUID

from sqlalchemy import UUID as SQLUUID
from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, mapped_column


class UUIDMixin:
    """
    Adds UUID primary key to models.
    """

    id: Mapped[UUID] = mapped_column(
        SQLUUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
    )


class TimestampMixin:
    """
    Adds creation and update timestamps.
    """

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )


class AuditMixin:
    """
    Tracks user who created or updated records.
    """

    created_by: Mapped[UUID | None] = mapped_column(
        SQLUUID(as_uuid=True),
        nullable=True,
    )

    updated_by: Mapped[UUID | None] = mapped_column(
        SQLUUID(as_uuid=True),
        nullable=True,
    )


class SoftDeleteMixin:
    """
    Provides logical (soft) delete functionality.

    Instead of physically removing records from the database,
    records are marked as deleted by setting the deleted_at timestamp.
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
        Returns True if the record has been soft deleted.
        """
        return self.deleted_at is not None

    def soft_delete(self) -> None:
        """
        Soft delete the record.

        Safe to call multiple times.
        """
        if self.deleted_at is None:
            self.deleted_at = datetime.now(UTC)

    def restore(self) -> None:
        """
        Restore a previously soft-deleted record.

        Safe to call multiple times.
        """
        self.deleted_at = None