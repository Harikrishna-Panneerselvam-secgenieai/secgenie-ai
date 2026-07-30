"""Investigation database model."""

from sqlalchemy.orm import Mapped, mapped_column

from app.database.models.base import Base


class Investigation(Base):
    """
    Represents a security investigation.
    """

    __tablename__ = "investigations"

    name: Mapped[str] = mapped_column(
        nullable=False
    )