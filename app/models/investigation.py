"""
Investigation model.

Represents a cybersecurity investigation executed by the
SecGenie multi-agent platform.
"""

from __future__ import annotations
from app.models.enums.investigation_priority import InvestigationPriority
from app.models.enums.investigation_status import InvestigationStatus
from datetime import datetime
from typing import Any

from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import Index
from sqlalchemy import JSON
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base import BaseModel


class Investigation(BaseModel):
    """
    Investigation entity.

    This is the root entity for every AI investigation.
    """

    __tablename__ = "investigations"

    __table_args__ = (
        Index("ix_investigation_status", "status"),
        Index("ix_investigation_owner", "owner_id"),
        Index("ix_investigation_priority", "priority"),
        Index("ix_investigation_created_at", "created_at"),
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        doc="Human-readable investigation title.",
    )

    description: Mapped[str | None] = mapped_column(
        String(2000),
        nullable=True,
        doc="Detailed investigation description.",
    )

    status: Mapped[InvestigationStatus] = mapped_column(
        Enum(
            InvestigationStatus,
            name="investigation_status",
        ),
        nullable=False,
        default=InvestigationStatus.CREATED,
        doc="Current lifecycle status.",
    )

    priority: Mapped[InvestigationPriority] = mapped_column(
        Enum(
            InvestigationPriority,
            name="investigation_priority",
        ),
        nullable=False,
        default=InvestigationPriority.MEDIUM,
        doc="Investigation priority.",
    )

    owner_id: Mapped[str | None] = mapped_column(
        String(36),
        nullable=True,
        doc="Owner user ID.",
    )

    # SQLAlchemy reserves the attribute name 'metadata'.
    # Keep the database column name as 'metadata' but expose it
    # through the Python attribute 'investigation_metadata'.
    investigation_metadata: Mapped[dict[str, Any]] = mapped_column(
        "metadata",
        JSON,
        nullable=False,
        default=dict,
        doc="Flexible metadata for AI agents.",
    )

    started_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        doc="Investigation execution start time.",
    )

    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        doc="Investigation execution completion time.",
    )

    def __repr__(self) -> str:
        return (
            f"Investigation("
            f"id={self.id}, "
            f"title={self.title!r}, "
            f"status={self.status.value})"
        )