"""
Investigation Service.

Contains business logic for investigation lifecycle management,
state transitions, validation, retry handling, and orchestration
between API layer and repository layer.
"""

from __future__ import annotations

from datetime import UTC, datetime
from uuid import UUID

from app.database.models.investigation import (
    Investigation,
    InvestigationStatus,
)
from app.repositories.investigation import InvestigationRepository
from app.schemas.investigation import (
    InvestigationCreate,
    InvestigationUpdate,
)
from app.schemas.pagination import PaginationParams
from app.services.base import BaseService
from app.services.exceptions import (
    InvalidStatusTransitionError,
    InvestigationNotFoundError,
    InvestigationRetryLimitExceededError,
)


class InvestigationService(BaseService):
    """
    Service layer for Investigation domain.

    Responsibilities:
    - Investigation creation
    - Lifecycle state management
    - Status transition validation
    - Retry handling
    - Business rule enforcement

    Does NOT:
    - Execute database queries directly
    - Execute AI agents
    - Handle HTTP concerns
    """

    # Allowed lifecycle transitions

    STATUS_TRANSITIONS: dict[
        InvestigationStatus,
        list[InvestigationStatus],
    ] = {
        InvestigationStatus.CREATED: [
            InvestigationStatus.QUEUED,
            InvestigationStatus.CANCELLED,
        ],
        InvestigationStatus.QUEUED: [
            InvestigationStatus.RUNNING,
            InvestigationStatus.CANCELLED,
        ],
        InvestigationStatus.RUNNING: [
            InvestigationStatus.COMPLETED,
            InvestigationStatus.FAILED,
            InvestigationStatus.CANCELLED,
        ],
        InvestigationStatus.FAILED: [
            InvestigationStatus.QUEUED,
            InvestigationStatus.CANCELLED,
        ],
        InvestigationStatus.COMPLETED: [],
        InvestigationStatus.CANCELLED: [],
    }

    def __init__(
        self,
        repository: InvestigationRepository,
    ) -> None:
        """
        Initialize Investigation Service.

        Args:
            repository:
                Investigation repository instance.
        """

        self.repository = repository

    # ---------------------------------------------------------
    # Create Investigation
    # ---------------------------------------------------------

    async def create_investigation(
        self,
        data: InvestigationCreate,
    ) -> Investigation:
        """
        Create new investigation.

        New investigations always start with CREATED status.

        Use case:
        User submits:
        "Investigate suspicious login attempts"

        System creates investigation record.
        """

        return await self.repository.create(
            **data.model_dump(),
            status=InvestigationStatus.CREATED,
        )

    # ---------------------------------------------------------
    # Get Investigation
    # ---------------------------------------------------------

    async def get_investigation(
        self,
        investigation_id: UUID,
    ) -> Investigation:
        """
        Retrieve investigation by ID.
        """

        investigation = await self.repository.get(investigation_id)

        if not investigation:
            raise InvestigationNotFoundError(investigation_id)

        return investigation

    async def list_investigations(
        self,
        pagination: PaginationParams,
    ) -> list[Investigation]:
        """
        Return paginated investigations.
        """

        return await self.repository.list(
            offset=pagination.offset,
            limit=pagination.limit,
        )

    # ---------------------------------------------------------
    # Update Investigation
    # ---------------------------------------------------------

    async def update_investigation(
        self,
        investigation_id: UUID,
        data: InvestigationUpdate,
    ) -> Investigation:
        """
        Update investigation details.
        """

        investigation = await self.get_investigation(investigation_id)

        update_data = data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(
                investigation,
                field,
                value,
            )

        return await self.repository.update(investigation)

    # ---------------------------------------------------------
    # Lifecycle Management
    # ---------------------------------------------------------

    async def transition_status(
        self,
        investigation_id: UUID,
        new_status: InvestigationStatus,
    ) -> Investigation:
        """
        Change investigation lifecycle state.

        Validates allowed state transitions.

        Example:

        RUNNING -> COMPLETED  ✅

        COMPLETED -> RUNNING ❌
        """

        investigation = await self.get_investigation(investigation_id)

        current_status = investigation.status

        allowed_states = self.STATUS_TRANSITIONS.get(
            current_status,
            [],
        )

        if new_status not in allowed_states:
            raise InvalidStatusTransitionError(
                current_status,
                new_status,
            )

        investigation.status = new_status

        return await self.repository.update(investigation)

    # ---------------------------------------------------------
    # Start Investigation
    # ---------------------------------------------------------

    async def start_investigation(
        self,
        investigation_id: UUID,
    ) -> Investigation:
        """
        Start investigation execution.

        Flow:

        CREATED
          |
          v
        QUEUED
          |
          v
        RUNNING
        """

        investigation = await self.transition_status(
            investigation_id,
            InvestigationStatus.QUEUED,
        )

        return await self.transition_status(
            investigation.id,
            InvestigationStatus.RUNNING,
        )

    # ---------------------------------------------------------
    # Complete Investigation
    # ---------------------------------------------------------

    async def complete_investigation(
        self,
        investigation_id: UUID,
    ) -> Investigation:
        """
        Mark investigation as completed.
        """

        investigation = await self.transition_status(
            investigation_id,
            InvestigationStatus.COMPLETED,
        )

        investigation.completed_at = datetime.now(UTC)

        return await self.repository.update(investigation)

    # ---------------------------------------------------------
    # Fail Investigation
    # ---------------------------------------------------------

    async def fail_investigation(
        self,
        investigation_id: UUID,
        reason: str,
    ) -> Investigation:
        """
        Mark investigation failed.

        Stores failure reason for audit/debugging.
        """

        investigation = await self.get_investigation(investigation_id)

        investigation.failure_reason = reason

        investigation.status = InvestigationStatus.FAILED

        return await self.repository.update(investigation)

    # ---------------------------------------------------------
    # Retry Handling
    # ---------------------------------------------------------

    async def retry_investigation(
        self,
        investigation_id: UUID,
        max_retry: int = 3,
    ) -> Investigation:
        """
        Retry failed investigation.

        FAILED -> QUEUED

        Prevents unlimited retries.
        """

        investigation = await self.get_investigation(investigation_id)

        retry_count = investigation.retry_count or 0

        if retry_count >= max_retry:
            raise InvestigationRetryLimitExceededError(investigation_id)

        investigation.retry_count = retry_count + 1

        investigation.status = InvestigationStatus.QUEUED

        return await self.repository.update(investigation)

    # ---------------------------------------------------------
    # Cancel Investigation
    # ---------------------------------------------------------

    async def cancel_investigation(
        self,
        investigation_id: UUID,
    ) -> Investigation:
        """
        Cancel active investigation.
        """

        return await self.transition_status(
            investigation_id,
            InvestigationStatus.CANCELLED,
        )

    # ---------------------------------------------------------
    # Delete / Restore
    # ---------------------------------------------------------

    async def delete_investigation(
        self,
        investigation_id: UUID,
    ) -> None:
        """
        Soft delete investigation.
        """

        investigation = await self.get_investigation(investigation_id)

        await self.repository.delete(investigation)

    async def restore_investigation(
        self,
        investigation_id: UUID,
    ) -> Investigation:
        """
        Restore soft deleted investigation.
        """

        investigation = await self.get_investigation(investigation_id)

        return await self.repository.restore(investigation)
