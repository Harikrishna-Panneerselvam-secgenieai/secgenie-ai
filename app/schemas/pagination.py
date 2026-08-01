"""
Reusable pagination schemas.

These models provide a consistent pagination interface across all list APIs.
"""

from __future__ import annotations

from math import ceil
from typing import Generic, TypeVar

from pydantic import BaseModel, ConfigDict, Field

T = TypeVar("T")


class PaginationParams(BaseModel):
    """
    Standard pagination request parameters.

    Used by list endpoints to control page number and page size.
    """

    model_config = ConfigDict(
        extra="forbid",
        frozen=True,
    )

    page: int = Field(
        default=1,
        ge=1,
        description="Page number (starting from 1).",
    )

    page_size: int = Field(
        default=20,
        ge=1,
        le=100,
        description="Maximum number of records per page.",
    )

    @property
    def offset(self) -> int:
        """Database OFFSET value."""
        return (self.page - 1) * self.page_size

    @property
    def limit(self) -> int:
        """Database LIMIT value."""
        return self.page_size


class PaginationMeta(BaseModel):
    """
    Pagination metadata returned with paginated responses.
    """

    model_config = ConfigDict(extra="forbid")

    page: int

    page_size: int

    total_items: int

    total_pages: int

    has_next: bool

    has_previous: bool

    @classmethod
    def create(
        cls,
        *,
        page: int,
        page_size: int,
        total_items: int,
    ) -> PaginationMeta:
        """
        Build pagination metadata from page information.
        """

        total_pages = max(1, ceil(total_items / page_size))

        return cls(
            page=page,
            page_size=page_size,
            total_items=total_items,
            total_pages=total_pages,
            has_next=page < total_pages,
            has_previous=page > 1,
        )


class PaginatedResponse(BaseModel, Generic[T]):
    """
    Generic paginated API response.
    """

    model_config = ConfigDict(extra="forbid")

    items: list[T]

    pagination: PaginationMeta
