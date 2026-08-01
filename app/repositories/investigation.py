"""
Investigation Repository.

Provides investigation-specific database operations.

Extends:
    BaseRepository

Features:
    - Status-based queries
    - Owner filtering
    - Active investigation queries
    - Search
    - Dashboard statistics
    - Stale investigation detection
"""

from __future__ import annotations

from datetime import UTC, datetime, timedelta
from typing import Any
from uuid import UUID

from sqlalchemy import func, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.enums.investigation_status import InvestigationStatus
from app.models.investigation import Investigation
from app.repositories.base import BaseRepository


class InvestigationRepository(
    BaseRepository[Investigation],
):
    """
    Repository for Investigation entity.

    Contains investigation-specific queries
    beyond generic CRUD operations.
    """

    def __init__(
        self,
        session: AsyncSession,
    ) -> None:
        """
        Initialize Investigation repository.
        """

        super().__init__(
            session,
            Investigation,
        )

    async def get_by_status(
        self,
        status: InvestigationStatus,
        *,
        include_deleted: bool = False,
    ) -> list[Investigation]:
        """
        Get investigations by lifecycle status.
        """

        return await self.list(
            filters={
                "status": status,
            },
            include_deleted=include_deleted,
        )

    async def get_by_owner(
        self,
        owner_id: UUID,
        *,
        include_deleted: bool = False,
    ) -> list[Investigation]:
        """
        Get investigations owned by a user.
        """

        return await self.list(
            filters={
                "owner_id": owner_id,
            },
            order_by="created_at",
            descending=True,
            include_deleted=include_deleted,
        )

    async def get_active(
        self,
        *,
        include_deleted: bool = False,
    ) -> list[Investigation]:
        """
        Return investigations currently executing.

        Active states:
        - CREATED
        - QUEUED
        - RUNNING
        """

        query = (
            select(Investigation)
            .where(
                Investigation.status.in_(
                    [
                        InvestigationStatus.CREATED,
                        InvestigationStatus.QUEUED,
                        InvestigationStatus.RUNNING,
                    ]
                )
            )
        )

        query = self._apply_soft_delete_filter(
            query,
            include_deleted,
        )

        result = await self.session.execute(query)

        return list(result.scalars().all())

    async def search(
        self,
        keyword: str,
        *,
        include_deleted: bool = False,
        limit: int = 100,
    ) -> list[Investigation]:
        """
        Search investigations by title or description.
        """

        query = select(Investigation)

        query = self._apply_soft_delete_filter(
            query,
            include_deleted,
        )

        search_pattern = f"%{keyword}%"

        query = query.where(
            or_(
                Investigation.title.ilike(
                    search_pattern,
                ),
                Investigation.description.ilike(
                    search_pattern,
                ),
            )
        )

        query = (
            query
            .order_by(
                Investigation.created_at.desc()
            )
            .limit(limit)
        )

        result = await self.session.execute(query)

        return list(result.scalars().all())

    async def get_recent(
        self,
        limit: int = 10,
        *,
        include_deleted: bool = False,
    ) -> list[Investigation]:
        """
        Return recently created investigations.
        """

        query = (
            select(Investigation)
            .order_by(
                Investigation.created_at.desc()
            )
            .limit(limit)
        )

        query = self._apply_soft_delete_filter(
            query,
            include_deleted,
        )

        result = await self.session.execute(query)

        return list(result.scalars().all())

    async def count_by_status(
        self,
        status: InvestigationStatus,
        *,
        include_deleted: bool = False,
    ) -> int:
        """
        Count investigations by status.
        """

        query = (
            select(
                func.count()
            )
            .select_from(Investigation)
            .where(
                Investigation.status == status,
            )
        )

        query = self._apply_soft_delete_filter(
            query,
            include_deleted,
        )

        result = await self.session.execute(query)

        return int(result.scalar_one())

    async def get_statistics(
        self,
        *,
        include_deleted: bool = False,
    ) -> dict[str, Any]:
        """
        Return investigation dashboard statistics.
        """

        total = await self.count(
            include_deleted=include_deleted,
        )

        statistics: dict[str, Any] = {
            "total": total,
        }

        for status in InvestigationStatus:
            statistics[
                status.value
            ] = await self.count_by_status(
                status,
                include_deleted=include_deleted,
            )

        return statistics

    async def get_completed_between(
        self,
        start_date: datetime,
        end_date: datetime,
        *,
        include_deleted: bool = False,
    ) -> list[Investigation]:
        """
        Return completed investigations
        within a time range.
        """

        query = (
            select(Investigation)
            .where(
                Investigation.completed_at >= start_date,
                Investigation.completed_at <= end_date,
            )
        )

        query = self._apply_soft_delete_filter(
            query,
            include_deleted,
        )

        result = await self.session.execute(query)

        return list(result.scalars().all())

    async def get_stale(
        self,
        hours: int = 24,
        *,
        include_deleted: bool = False,
    ) -> list[Investigation]:
        """
        Return investigations stuck in execution.

        Useful for:
        - watchdog services
        - scheduler recovery
        """

        threshold = datetime.now(UTC) - timedelta(
            hours=hours,
        )

        query = (
            select(Investigation)
            .where(
                Investigation.status
                == InvestigationStatus.RUNNING,
                Investigation.updated_at < threshold,
            )
        )

        query = self._apply_soft_delete_filter(
            query,
            include_deleted,
        )

        result = await self.session.execute(query)

        return list(result.scalars().all())