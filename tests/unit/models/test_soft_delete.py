"""
Unit tests for SoftDeleteMixin.
"""

from __future__ import annotations

from datetime import UTC, datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.models.base import Base


class DummyModel(Base):
    """Simple model used for testing SoftDeleteMixin."""

    __tablename__ = "dummy_model"

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        default="Test Model",
    )


class TestSoftDeleteMixin:
    """Test suite for SoftDeleteMixin."""

    def test_new_object_is_not_deleted(self) -> None:
        """A newly created object should not be marked as deleted."""

        model = DummyModel()

        assert model.deleted_at is None
        assert model.is_deleted is False

    def test_soft_delete_sets_deleted_at(self) -> None:
        """soft_delete() should set deleted_at."""

        model = DummyModel()

        model.soft_delete()

        assert model.deleted_at is not None
        assert isinstance(model.deleted_at, datetime)
        assert model.deleted_at.tzinfo == UTC
        assert model.is_deleted is True

    def test_restore_clears_deleted_at(self) -> None:
        """restore() should clear deleted_at."""

        model = DummyModel()

        model.soft_delete()
        assert model.is_deleted is True

        model.restore()

        assert model.deleted_at is None
        assert model.is_deleted is False

    def test_soft_delete_is_idempotent(self) -> None:
        """Calling soft_delete() twice should preserve the original timestamp."""

        model = DummyModel()

        model.soft_delete()
        first_timestamp = model.deleted_at

        model.soft_delete()

        assert model.deleted_at == first_timestamp

    def test_restore_is_idempotent(self) -> None:
        """Calling restore() multiple times should not fail."""

        model = DummyModel()

        model.restore()
        model.restore()

        assert model.deleted_at is None
        assert model.is_deleted is False

    def test_delete_restore_delete_cycle(self) -> None:
        """A model should support delete -> restore -> delete."""

        model = DummyModel()

        model.soft_delete()
        first_timestamp = model.deleted_at

        model.restore()

        assert model.deleted_at is None
        assert model.is_deleted is False

        model.soft_delete()

        assert model.deleted_at is not None
        assert model.is_deleted is True
        assert model.deleted_at != first_timestamp