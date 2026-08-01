"""
Standard error response schemas for SecGenie.ai.
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field

from app.schemas.responses import ResponseMetadata


class ErrorDetail(BaseModel):
    """
    Standard error information returned by the API.
    """

    code: str = Field(
        ...,
        description="Machine-readable error code.",
    )

    message: str = Field(
        ...,
        description="Human-readable error message.",
    )

    details: dict[str, Any] = Field(
        default_factory=dict,
        description="Additional error details.",
    )

    request_id: str | None = Field(
        default=None,
        description="Unique request identifier.",
    )

    correlation_id: str | None = Field(
        default=None,
        description="Correlation identifier used to trace requests across services.",
    )


class ErrorResponse(BaseModel):
    """
    Standard error response returned by all API endpoints.
    """

    success: bool = Field(
        default=False,
    )

    error: ErrorDetail

    metadata: ResponseMetadata | None = None