"""
Base Service Layer.

Provides reusable business operations for all application services.

Responsibilities:
- Repository dependency management
- Database transaction handling
- Common CRUD operations
- Validation lifecycle hooks
- Shared service behavior

Architecture:

API Layer
    |
    v
Service Layer (Business Logic)
    |
    v
Repository Layer (Database Access)
    |
    v
Database
"""

from typing import Any, Generic, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession

from app.services.exceptions import (
    EntityNotFoundError,
)


ModelType = TypeVar("ModelType")
RepositoryType = TypeVar("RepositoryType")


class BaseService(
    Generic[ModelType, RepositoryType],
):
    """
    Generic base service.

    All domain services should inherit from this class.

    Example:

        class InvestigationService(
            BaseService[
                Investigation,
                InvestigationRepository,
            ]
        ):
            pass
    """

    def __init__(
        self,
        repository: RepositoryType,
        session: AsyncSession,
    ) -> None:
        """
        Initialize service.

        Args:
            repository:
                Repository responsible for data access.

            session:
                SQLAlchemy async database session.
        """

        self.repository = repository
        self.session = session

    # ------------------------------------------------------------------
    # Transaction Management
    # ------------------------------------------------------------------

    async def commit(self) -> None:
        """
        Commit current database transaction.
        """

        await self.session.commit()

    async def rollback(self) -> None:
        """
        Rollback current database transaction.
        """

        await self.session.rollback()

    async def flush(self) -> None:
        """
        Flush pending database changes.

        Useful when database generated values
        are required before commit.
        """

        await self.session.flush()

    # ------------------------------------------------------------------
    # Validation Hooks
    # ------------------------------------------------------------------

    async def validate_create(
        self,
        data: Any,
    ) -> None:
        """
        Hook executed before entity creation.

        Child services can override this.

        Example:

            Check duplicate investigation.
            Validate permissions.
            Validate required fields.

        """

    async def validate_update(
        self,
        entity: ModelType,
        data: Any,
    ) -> None:
        """
        Hook executed before entity update.

        Child services can override this.

        Example:

            Validate status transitions.
            Validate lifecycle rules.
        """

    async def validate_delete(
        self,
        entity: ModelType,
    ) -> None:
        """
        Hook executed before entity deletion.

        Child services can override this.

        Example:

            Prevent deleting active investigations.
        """

    # ------------------------------------------------------------------
    # Common CRUD Operations
    # ------------------------------------------------------------------

    async def get(
        self,
        entity_id: Any,
    ) -> ModelType:
        """
        Retrieve entity by ID.

        Raises:
            EntityNotFoundError:
                If entity does not exist.
        """

        entity = await self.repository.get(
            entity_id,
        )

        if entity is None:
            raise EntityNotFoundError(
                entity_name=self.repository.model.__name__,
                entity_id=str(entity_id),
            )

        return entity

    async def create(
        self,
        data: Any,
    ) -> ModelType:
        """
        Create a new entity.

        Flow:

        validate
            |
        repository create
            |
        commit
            |
        return entity
        """

        await self.validate_create(
            data,
        )

        entity = await self.repository.create(
            data,
        )

        await self.commit()

        return entity

    async def update(
        self,
        entity_id: Any,
        data: Any,
    ) -> ModelType:
        """
        Update existing entity.
        """

        entity = await self.get(
            entity_id,
        )

        await self.validate_update(
            entity,
            data,
        )

        updated_entity = await self.repository.update(
            entity,
            data,
        )

        await self.commit()

        return updated_entity

    async def delete(
        self,
        entity_id: Any,
    ) -> None:
        """
        Delete entity.

        Supports repository-level
        soft delete implementation.
        """

        entity = await self.get(
            entity_id,
        )

        await self.validate_delete(
            entity,
        )

        await self.repository.delete(
            entity,
        )

        await self.commit()