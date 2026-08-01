"""Tests for the BaseModel."""

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models import BaseModel


class SampleModel(BaseModel):
    """
    Temporary model used to verify BaseModel inheritance.
    """

    __tablename__ = "sample_models"

    name: Mapped[str] = mapped_column(String(100))


def test_base_model_inheritance():
    """
    Verify that BaseModel provides all common fields.
    """

    columns = SampleModel.__table__.columns.keys()

    expected_columns = {
        "id",
        "created_at",
        "updated_at",
        "created_by",
        "updated_by",
        "is_deleted",
        "deleted_at",
        "deleted_by",
        "name",
    }

    assert expected_columns.issubset(set(columns))