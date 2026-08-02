"""
Investigation model.

Represents a cybersecurity investigation executed by the
SecGenie multi-agent platform.
"""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any
from uuid import UUID

from sqlalchemy import JSON, DateTime, Enum, ForeignKey, Index, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel
from app.models.enums.investigation_priority import InvestigationPriority
from app.models.enums.investigation_status import InvestigationStatus

if TYPE_CHECKING:
    from app.models.evidence import Evidence
    from app.models.finding import Finding
    from app.models.investigation_task import InvestigationTask
    from app.models.timeline import InvestigationTimeline
    from app.models.user import User


class Investigation(BaseModel):
    """
    Investigation entity.

    Root entity for every cybersecurity investigation
    executed by the SecGenie multi-agent platform.
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
        doc="Current investigation lifecycle status.",
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

    owner_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True,
        doc="User who owns this investigation.",
    )

    # SQLAlchemy reserves the attribute name 'metadata'.
    # Database column remains 'metadata', Python attribute is
    # investigation_metadata.
    investigation_metadata: Mapped[dict[str, Any]] = mapped_column(
        "metadata",
        JSON,
        nullable=False,
        default=dict,
        doc="Flexible metadata used by AI agents.",
    )

    started_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        doc="Investigation execution start time.",
    )

    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        doc="Investigation completion time.",
    )

    # =====================================================
    # Relationships
    # =====================================================

    owner: Mapped[User | None] = relationship(
        "User",
        foreign_keys=[owner_id],
        back_populates="investigations",
    )

    findings: Mapped[list[Finding]] = relationship(
        "Finding",
        back_populates="investigation",
        cascade="all, delete-orphan",
    )

    evidence: Mapped[list[Evidence]] = relationship(
        "Evidence",
        back_populates="investigation",
        cascade="all, delete-orphan",
    )

    tasks: Mapped[list[InvestigationTask]] = relationship(
        "InvestigationTask",
        back_populates="investigation",
        cascade="all, delete-orphan",
    )

    timeline: Mapped[list[InvestigationTimeline]] = relationship(
        "InvestigationTimeline",
        back_populates="investigation",
        cascade="all, delete-orphan",
        order_by="InvestigationTimeline.event_time",
    )

    def __repr__(self) -> str:
        return (
            f"Investigation("
            f"id={self.id}, "
            f"title={self.title!r}, "
            f"status={self.status.value})"
        )
