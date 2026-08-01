"""
Investigation task model.

Tracks execution of AI agent tasks
within an investigation.
"""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import JSON, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel

if TYPE_CHECKING:
    from app.models.investigation import Investigation


class InvestigationTask(BaseModel):
    """
    Represents an individual AI agent task execution.
    """

    __tablename__ = "investigation_tasks"

    investigation_id: Mapped[str] = mapped_column(
        ForeignKey("investigations.id"),
        nullable=False,
        index=True,
        doc="Related investigation ID.",
    )

    agent_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        doc="Executing AI agent name.",
    )

    task_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        doc="Type of task executed.",
    )

    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="PENDING",
        doc="Task execution status.",
    )

    started_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        doc="Task start time.",
    )

    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        doc="Task completion time.",
    )

    result: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
        doc="Agent execution result.",
    )

    error_message: Mapped[str | None] = mapped_column(
        String(2000),
        nullable=True,
        doc="Failure reason if task failed.",
    )

    # ---------------------------------------------------------
    # Relationship
    # ---------------------------------------------------------

    investigation: Mapped[Investigation] = relationship(
        "Investigation",
        back_populates="tasks",
    )

    def __repr__(self) -> str:
        return (
            f"InvestigationTask("
            f"id={self.id}, "
            f"agent={self.agent_name!r}, "
            f"status={self.status!r})"
        )