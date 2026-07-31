"""
Finding model.

Represents security findings generated during an investigation.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


if TYPE_CHECKING:
    from app.models.investigation import Investigation
    from app.models.evidence import Evidence


class Finding(BaseModel):
    """
    Security finding entity.

    Stores observations and conclusions
    produced by AI agents during an investigation.
    """

    __tablename__ = "findings"

    investigation_id: Mapped[str] = mapped_column(
        ForeignKey("investigations.id"),
        nullable=False,
        index=True,
        doc="Related investigation ID.",
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        doc="Finding title.",
    )

    description: Mapped[str | None] = mapped_column(
        String(2000),
        nullable=True,
        doc="Detailed finding description.",
    )

    severity: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        doc="Finding severity.",
    )

    category: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        doc="Finding category.",
    )

    confidence_score: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
        doc="AI confidence score.",
    )

    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="OPEN",
        doc="Finding lifecycle status.",
    )

    # ---------------------------------------------------------
    # Relationships
    # ---------------------------------------------------------

    investigation: Mapped["Investigation"] = relationship(
        "Investigation",
        back_populates="findings",
    )

    evidence: Mapped[list["Evidence"]] = relationship(
        "Evidence",
        back_populates="finding",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return (
            f"Finding("
            f"id={self.id}, "
            f"title={self.title!r}, "
            f"severity={self.severity!r})"
        )