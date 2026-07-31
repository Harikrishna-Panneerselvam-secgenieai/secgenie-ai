"""
Audit log model.

Tracks user and system actions
for security and compliance.
"""

from __future__ import annotations

from sqlalchemy import JSON
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base import BaseModel


class AuditLog(BaseModel):
    """
    Represents an audit event.
    """

    __tablename__ = "audit_logs"

    user_id: Mapped[str | None] = mapped_column(
        String(36),
        nullable=True,
        index=True,
        doc="User who performed action.",
    )

    action: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        doc="Action performed.",
    )

    entity_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        doc="Entity affected.",
    )

    entity_id: Mapped[str | None] = mapped_column(
        String(36),
        nullable=True,
        doc="Affected entity ID.",
    )

    audit_metadata: Mapped[dict] = mapped_column(
        "metadata",
        JSON,
        nullable=False,
        default=dict,
        doc="Additional audit information.",
    )

    def __repr__(self) -> str:
        return (
            f"AuditLog("
            f"id={self.id}, "
            f"action={self.action!r})"
        )