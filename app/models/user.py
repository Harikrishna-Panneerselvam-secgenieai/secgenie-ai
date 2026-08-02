"""
User model.

Represents users interacting with the SecGenie platform.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel

if TYPE_CHECKING:
    from app.models.investigation import Investigation


class User(BaseModel):
    """
    Platform user entity.
    """

    __tablename__ = "users"

    username: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        doc="User display name.",
    )

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
        index=True,
        doc="User email address.",
    )

    role: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        doc="User role.",
    )

    investigations: Mapped[list[Investigation]] = relationship(
        "Investigation",
        back_populates="owner",
    )

    def __repr__(self) -> str:
        return f"User(id={self.id}, email={self.email!r})"
