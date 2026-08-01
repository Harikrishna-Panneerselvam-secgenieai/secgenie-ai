"""
Standard API response schemas for SecGenie.ai.
"""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Any, Generic, TypeVar

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

    data: T = Field(
        description="Response payload.",
    )

    metadata: ResponseMetadata = Field(
        default_factory=ResponseMetadata,
    )


class MessageResponse(BaseModel):
    """
    Response for operations without payload.

    Examples:
    - Delete
    - Restore
    - Cancel
    - Retry
    """

    success: bool = Field(
        default=True,
        description="Operation status.",
    )

    message: str = Field(
        description="Operation result message.",
    )

    metadata: ResponseMetadata = Field(
        default_factory=ResponseMetadata,
    )


class ErrorResponse(BaseModel):
    """
    Standard error response returned by the API.
    """

    success: bool = Field(
        default=False,
        description="Always false for error responses.",
    )

    message: str = Field(
        description="Human-readable error message.",
    )

    error_code: str = Field(
        description="Application-specific error code.",
    )

    details: dict[str, Any] | None = Field(
        default=None,
        description="Additional error details.",
    )

    metadata: ResponseMetadata = Field(
        default_factory=ResponseMetadata,
    )


class ValidationErrorItem(BaseModel):
    """
    Represents a single validation error.
    """

    field: str = Field(
        description="Field that failed validation.",
    )

    message: str = Field(
        description="Validation error message.",
    )

    type: str | None = Field(
        default=None,
        description="Validation error type.",
    )

    input: Any | None = Field(
        default=None,
        description="Input value that caused validation failure.",
    )


class ValidationErrorResponse(BaseModel):
    """
    Standard validation error response.
    """

    success: bool = Field(
        default=False,
        description="Always false for validation errors.",
    )

    message: str = Field(
        default="Validation failed.",
        description="Validation failure summary.",
    )

    errors: list[ValidationErrorItem] = Field(
        description="List of validation errors.",
    )

    metadata: ResponseMetadata = Field(
        default_factory=ResponseMetadata,
    )


class PaginationMetadata(BaseModel):
    """
    Pagination information.
    """

    page: int = Field(
        description="Current page number.",
    )

    page_size: int = Field(
        description="Number of items per page.",
    )

    total: int = Field(
        description="Total number of records.",
    )

    total_pages: int = Field(
        description="Total number of available pages.",
    )

    has_next: bool = Field(
        description="Whether another page exists.",
    )

    has_previous: bool = Field(
        description="Whether a previous page exists.",
    )


class PaginatedResponse(BaseModel, Generic[T]):
    """
    Standard paginated API response.
    """

    success: bool = Field(
        default=True,
        description="Always true for successful responses.",
    )

    message: str = Field(
        default="Success",
        description="Human-readable success message.",
    )

    data: list[T] = Field(
        description="List of returned records.",
    )

    pagination: PaginationMetadata = Field(
        description="Pagination metadata.",
    )

    metadata: ResponseMetadata = Field(
        default_factory=ResponseMetadata,
    )
