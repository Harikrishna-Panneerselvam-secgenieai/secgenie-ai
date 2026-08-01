"""
Generic Base Repository.

Provides reusable asynchronous CRUD operations for SQLAlchemy ORM models.

Features
--------
- Generic repository using Python Generics
- SQLAlchemy 2.0 async support
- CRUD operations
- Pagination
- Filtering
- Sorting
- Soft delete awareness
- Transaction helpers
"""

from __future__ import annotations

from typing import Any, Generic, TypeVar

from sqlalchemy import Select, asc, desc, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.base import BaseModel

ModelType = TypeVar(
    "ModelType",
    bound=BaseModel,
)


class BaseRepository(Generic[ModelType]):
    """
    Generic repository for SQLAlchemy ORM models.

    Every entity repository should inherit from this class.

    Example
    -------
    class InvestigationRepository(
        BaseRepository[Investigation]
    ):
        def __init__(self, session: AsyncSession):
            super().__init__(session, Investigation)
    """

    def __init__(
        self,
        session: AsyncSession,
        model: type[ModelType],
    ) -> None:
        """
        Initialize repository.

        Parameters
        ----------
        session:
            Async SQLAlchemy session.

        model:
            SQLAlchemy ORM model class.
        """
        self.session = session
        self.model = model

    # ==========================================================
    # Internal Helpers
    # ==========================================================

    def _base_query(self) -> Select[tuple[ModelType]]:
        """
        Return a base SELECT statement.

        Child repositories can extend this query if required.
        """
        return select(self.model)

    def _apply_soft_delete_filter(
        self,
        query: Select[Any],
        include_deleted: bool,
    ) -> Select[Any]:
        """
        Exclude soft deleted rows unless requested.
        """

        if (
            hasattr(self.model, "deleted_at")
            and not include_deleted
        ):
            query = query.where(
                self.model.deleted_at.is_(None)
            )

        return query

    @property
    def model_name(self) -> str:
        """Return ORM model name."""
        return self.model.__name__

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(model={self.model_name})"
        )

    async def create(
        self,
        **kwargs: Any,
    ) -> ModelType:
        """
        Create a new record.
        """

        instance = self.model(**kwargs)

        self.session.add(instance)

        await self.session.flush()
        await self.session.refresh(instance)

        return instance


    async def update(
        self,
        instance: ModelType,
        **kwargs: Any,
    ) -> ModelType:
        """
        Update an existing model instance.
        """

        for field, value in kwargs.items():
            setattr(instance, field, value)

        await self.session.flush()
        await self.session.refresh(instance)

        return instance

    async def delete(
        self,
        instance: ModelType,
    ) -> None:
        """
        Permanently delete a model instance.
        """

        await self.session.delete(instance)

        await self.session.flush()

    async def soft_delete(
        self,
        instance: ModelType,
    ) -> ModelType:
        """
        Soft delete a model instance.
        """

        if hasattr(instance, "soft_delete"):
            instance.soft_delete()

        await self.session.flush()
        await self.session.refresh(instance)

        return instance

    async def restore(
        self,
        instance: ModelType,
    ) -> ModelType:
        """
        Restore a soft deleted model.
        """

        if hasattr(instance, "restore"):
            instance.restore()

        await self.session.flush()
        await self.session.refresh(instance)

        return instance

    async def commit(self) -> None:
        """
        Commit current transaction.
        """

        await self.session.commit()

    async def rollback(self) -> None:
        """
        Roll back current transaction.
        """

        await self.session.rollback()

    async def flush(self) -> None:
        """
        Flush pending changes.
        """

        await self.session.flush()

async def refresh(
    self,
    instance: ModelType,
) -> None:
    """
    Refresh model from database.
    """

    await self.session.refresh(instance)


    async def get_by_id(
        self,
        id: Any,
        *,
        include_deleted: bool = False,
    ) -> ModelType | None:
        """
        Return a model by primary key.
        """

        query = self._base_query().where(
            self.model.id == id
        )

        query = self._apply_soft_delete_filter(
            query,
            include_deleted,
        )

        result = await self.session.execute(query)

        return result.scalar_one_or_none()

    async def get_one(
        self,
        *,
        include_deleted: bool = False,
        **filters: Any,
    ) -> ModelType | None:
        """
        Return the first record matching filters.
        """

        query = self._base_query()

        query = self._apply_soft_delete_filter(
            query,
            include_deleted,
        )

        for field, value in filters.items():
            column = getattr(self.model, field)
            query = query.where(column == value)

        result = await self.session.execute(query)

        return result.scalar_one_or_none()

    async def exists(
        self,
        **filters: Any,
    ) -> bool:
        """
        Return True if a matching record exists.
        """

        return (
            await self.get_one(**filters)
        ) is not None

    async def count(
        self,
        *,
        include_deleted: bool = False,
    ) -> int:
        """
        Return total number of records.
        """

        query = select(
            func.count()
        ).select_from(self.model)

        query = self._apply_soft_delete_filter(
            query,
            include_deleted,
        )

        result = await self.session.execute(query)

        return int(result.scalar_one())

    async def list(
        self,
        *,
        filters: dict[str, Any] | None = None,
        order_by: str | None = None,
        descending: bool = False,
        offset: int = 0,
        limit: int = 100,
        include_deleted: bool = False,
    ) -> list[ModelType]:
        """
        Return a list of records.

        Supports:
        - filtering
        - sorting
        - pagination
        """

        query = self._base_query()

        query = self._apply_soft_delete_filter(
            query,
            include_deleted,
        )

        if filters:
            for field, value in filters.items():
                column = getattr(self.model, field)
                query = query.where(column == value)

        if order_by:
            column = getattr(self.model, order_by)

            query = query.order_by(
                desc(column)
                if descending
                else asc(column)
            )

        query = query.offset(offset).limit(limit)

        result = await self.session.execute(query)

        return list(result.scalars().all())