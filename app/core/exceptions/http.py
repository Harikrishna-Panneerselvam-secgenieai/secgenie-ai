"""
HTTP exception definitions for SecGenie.ai.

This module will contain reusable HTTP exception classes such as:

- BadRequestError
- UnauthorizedError
- ForbiddenError
- NotFoundError
- ConflictError

These classes will inherit from AppException.
"""

from __future__ import annotations

from typing import Any

from app.core.exceptions.base import AppException


class BadRequestError(AppException):
    """
    Raised when the client sends an invalid request.
    """

    def __init__(
        self,
        message: str = "Bad request.",
        *,
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(
            message=message,
            status_code=400,
            error_code="BAD_REQUEST",
            details=details,
        )


class UnauthorizedError(AppException):
    """
    Raised when authentication fails.
    """

    def __init__(
        self,
        message: str = "Authentication required.",
        *,
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(
            message=message,
            status_code=401,
            error_code="UNAUTHORIZED",
            details=details,
        )


class ForbiddenError(AppException):
    """
    Raised when the user is not allowed to perform an action.
    """

    def __init__(
        self,
        message: str = "Access forbidden.",
        *,
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(
            message=message,
            status_code=403,
            error_code="FORBIDDEN",
            details=details,
        )


class NotFoundError(AppException):
    """
    Raised when a requested resource does not exist.
    """

    def __init__(
        self,
        message: str = "Resource not found.",
        *,
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(
            message=message,
            status_code=404,
            error_code="NOT_FOUND",
            details=details,
        )


class ConflictError(AppException):
    """
    Raised when a resource already exists or a conflict occurs.
    """

    def __init__(
        self,
        message: str = "Resource conflict.",
        *,
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(
            message=message,
            status_code=409,
            error_code="CONFLICT",
            details=details,
        )


class TooManyRequestsError(AppException):
    """
    Raised when rate limits are exceeded.
    """

    def __init__(
        self,
        message: str = "Too many requests.",
        *,
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(
            message=message,
            status_code=429,
            error_code="TOO_MANY_REQUESTS",
            details=details,
        )


class InternalServerError(AppException):
    """
    Raised for unexpected server-side failures.
    """

    def __init__(
        self,
        message: str = "Internal server error.",
        *,
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(
            message=message,
            status_code=500,
            error_code="INTERNAL_SERVER_ERROR",
            details=details,
        )
