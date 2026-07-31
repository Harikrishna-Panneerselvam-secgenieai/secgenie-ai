"""
Investigation timeline model.

Stores chronological events generated during
investigation execution.
"""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


if TYPE_CHECKING:
    from app.models.investigation import Investigation


class InvestigationTimeline(BaseModel):
    """
    Timeline event for an investigation.

    Used for auditability and tracking
    AI agent execution flow.
    """

    __tablename__ = "investigation_timelines"

    investigation_id: Mapped[str] = mapped_column(
        ForeignKey("investigations.id"),
        nullable=False,
        index=True,
        doc="Related investigation ID.",
    )

    event_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        doc="Timeline event type.",
    )

    message: Mapped[str] = mapped_column(
        String(2000),
        nullable=False,
        doc="Human-readable event message.",
    )

    agent_name: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
        doc="Agent responsible for event.",
    )

    event_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.utcnow,
        doc="Event timestamp.",
    )

    # ---------------------------------------------------------
    # Relationship
    # ---------------------------------------------------------

    investigation: Mapped["Investigation"] = relationship(
        "Investigation",
        back_populates="timeline",
    )

    def __repr__(self) -> str:
        return (
            f"InvestigationTimeline("
            f"id={self.id}, "
            f"type={self.event_type!r})"
        )