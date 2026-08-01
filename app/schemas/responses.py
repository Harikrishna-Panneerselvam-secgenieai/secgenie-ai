"""
Standard API response schemas for SecGenie.ai.
"""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class ResponseMetadata(BaseModel):
    """
    Common metadata attached to every API response.
    Used for tracing and observability.
    """

    request_id: str | None = Field(
        default=None,
        description="Unique request identifier.",
    )

    correlation_id: str | None = Field(
        default=None,
        description="Distributed tracing identifier.",
    )

    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        description="Response creation timestamp.",
    )


class SuccessResponse(BaseModel, Generic[T]):
    """
    Standard successful API response.
    """

    success: bool = Field(
        default=True,
        description="Always true for successful responses.",
    )

    message: str = Field(
        default="Success",
        description="Human-readable success message.",
    )

    data: T

    metadata: ResponseMetadata = Field(
        default_factory=ResponseMetadata,
    )


class MessageResponse(BaseModel):
    """
    Response for operations without payload.
    Example:
    - delete success
    - restore success
    """

    success: bool = Field(default=True)

    message: str

    metadata: ResponseMetadata = Field(
        default_factory=ResponseMetadata,
    )


class PaginationMetadata(BaseModel):
    """
    Pagination information.
    """

    page: int

    page_size: int

    total: int

    total_pages: int


class PaginatedResponse(BaseModel, Generic[T]):
    """
    Standard paginated API response.
    """

    success: bool = Field(default=True)

    message: str = Field(
        default="Success",
    )

    data: list[T]

    pagination: PaginationMetadata

    metadata: ResponseMetadata = Field(
        default_factory=ResponseMetadata,
    )