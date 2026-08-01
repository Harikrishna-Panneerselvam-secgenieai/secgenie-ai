"""
Standard API response schemas for SecGenie.ai.
"""

from __future__ import annotations

from typing import Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class SuccessResponse(BaseModel, Generic[T]):
    """
    Standard success response.
    """

    success: bool = Field(
        default=True,
        description="Always true for successful responses.",
    )

    data: T


class MessageResponse(BaseModel):
    """
    Standard response for simple success messages.
    """

    success: bool = Field(default=True)

    message: str


class PaginatedResponse(BaseModel, Generic[T]):
    """
    Standard paginated response.
    """

    success: bool = Field(default=True)

    data: list[T]

    total: int

    page: int

    page_size: int