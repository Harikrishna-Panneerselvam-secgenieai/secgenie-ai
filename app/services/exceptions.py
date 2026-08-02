"""
Service layer exception hierarchy.

This module contains exceptions raised during business logic execution.

Service exceptions represent:
- Business rule violations
- Entity lifecycle failures
- Validation failures
- Operation failures

They are handled by API exception handlers and converted
into appropriate HTTP responses.
"""

from __future__ import annotations

from uuid import UUID


class ServiceError(Exception):
    """
    Base exception for all service layer errors.

    All custom service exceptions should inherit from this class.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        self.message = message
        super().__init__(message)


class EntityNotFoundError(ServiceError):
    """
    Raised when a requested entity does not exist.

    Example:
        Investigation ID does not exist.
        Finding record cannot be located.
    """

    def __init__(
        self,
        entity_name: str,
        entity_id: str | None = None,
    ) -> None:
        if entity_id:
            message = f"{entity_name} with id '{entity_id}' was not found"
        else:
            message = f"{entity_name} was not found"

        super().__init__(message)

        self.entity_name = entity_name
        self.entity_id = entity_id


class ValidationError(ServiceError):
    """
    Raised when business validation fails.

    Examples:
        Invalid investigation status transition.
        Missing required evidence.
        Invalid workflow state.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        super().__init__(message)


class BusinessRuleViolationError(ServiceError):
    """
    Raised when a domain business rule is violated.

    Examples:
        Cannot modify completed investigation.
        Cannot delete active evidence.
        Cannot execute duplicate workflow.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        super().__init__(message)


class OperationFailedError(ServiceError):
    """
    Raised when a service operation fails unexpectedly.

    Examples:
        Failed workflow execution.
        External service dependency failure.
        Transaction failure.
    """

    def __init__(
        self,
        operation: str,
        reason: str | None = None,
    ) -> None:
        if reason:
            message = f"Operation '{operation}' failed: {reason}"
        else:
            message = f"Operation '{operation}' failed"

        super().__init__(message)

        self.operation = operation
        self.reason = reason


class DuplicateEntityError(ServiceError):
    """Raised when attempting to create a duplicate entity."""

    def __init__(self, entity_name: str, identifier: str | None = None):
        ...
        self.entity_name = entity_name
        self.identifier = identifier


class InvestigationNotFoundError(EntityNotFoundError):
    """Raised when an investigation cannot be found."""

    def __init__(self, investigation_id: UUID) -> None:
        super().__init__(
            entity_name="Investigation",
            entity_id=str(investigation_id),
        )


class InvalidStatusTransitionError(BusinessRuleViolationError):
    """Raised when an invalid investigation status transition is attempted."""

    def __init__(self, current_status: str, target_status: str) -> None:
        super().__init__(
            f"Cannot transition investigation from "
            f"'{current_status}' to '{target_status}'."
        )


class InvestigationRetryLimitExceededError(BusinessRuleViolationError):
    """Raised when the retry limit for an investigation has been exceeded."""

    def __init__(self, investigation_id: UUID) -> None:
        super().__init__(f"Retry limit exceeded for investigation {investigation_id}.")
