"""Reusable SQLAlchemy model mixins."""

import uuid
from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, UUID as SQLUUID, func
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
    Provides soft delete support.
    """

    deleted_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )