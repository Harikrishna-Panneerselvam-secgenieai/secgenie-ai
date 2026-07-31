"""Reusable SQLAlchemy model mixins."""

from __future__ import annotations

import uuid
from datetime import datetime
from datetime import timezone

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class UUIDPrimaryKeyMixin:
    """
    Adds a UUID primary key to a model.
    """

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )


class TimestampMixin:
    """
    Automatically tracks record creation and updates.
    """

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )


class AuditMixin:
    """
    Tracks which user created and last updated the record.
    """

    created_by: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    updated_by: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )


class SoftDeleteMixin:
    """
    Adds soft delete support.
    """

    is_deleted: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    deleted_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    deleted_by: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    def soft_delete(self, deleted_by: str | None = None) -> None:
        """
        Mark the record as deleted.
        """
        self.is_deleted = True
        self.deleted_at = datetime.now(timezone.utc)
        self.deleted_by = deleted_by

    def restore(self) -> None:
        """
        Restore a previously soft deleted record.
        """
        self.is_deleted = False
        self.deleted_at = None
        self.deleted_by = None