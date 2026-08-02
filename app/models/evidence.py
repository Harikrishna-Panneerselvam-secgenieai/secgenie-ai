"""
Evidence model.

Stores evidence collected during investigations.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import JSON, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel

if TYPE_CHECKING:
    from app.models.finding import Finding
    from app.models.investigation import Investigation


class Evidence(BaseModel):
    """
    Evidence entity.

    Represents artifacts collected by AI agents
    during investigation execution.
    """

    __tablename__ = "evidence"

    investigation_id: Mapped[str] = mapped_column(
        ForeignKey("investigations.id"),
        nullable=False,
        index=True,
        doc="Related investigation ID.",
    )

    finding_id: Mapped[str | None] = mapped_column(
        ForeignKey("findings.id"),
        nullable=True,
        index=True,
        doc="Related finding ID.",
    )

    evidence_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        doc="Evidence category.",
    )

    source: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        doc="Evidence source.",
    )

    data: Mapped[dict] = mapped_column(
        JSON,
        nullable=False,
        default=dict,
        doc="Evidence payload.",
    )

    collected_by: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
        doc="Agent or user who collected evidence.",
    )

    # ---------------------------------------------------------
    # Relationships
    # ---------------------------------------------------------

    investigation: Mapped[Investigation] = relationship(
        "Investigation",
        back_populates="evidence",
    )

    finding: Mapped[Finding | None] = relationship(
        "Finding",
        back_populates="evidence",
    )

    def __repr__(self) -> str:
        return (
            f"Evidence("
            f"id={self.id}, "
            f"type={self.evidence_type!r}, "
            f"source={self.source!r})"
        )
