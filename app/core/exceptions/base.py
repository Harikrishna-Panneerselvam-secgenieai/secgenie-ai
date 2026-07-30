"""
Base exception definitions for SecGenie.ai.

This module contains the base exception class that all
custom application exceptions will inherit from.

Implementation of AppException will be added in Step 2.
"""

from __future__ import annotations

from typing import Any


class AppException(Exception):
    """
    Base exception for all application-specific exceptions.

    Attributes:
        status_code: HTTP status code to return.
        error_code: Machine-readable error identifier.
        message: Human-readable error message.
        details: Optional additional error information.
    """

    def __init__(
        self,
        message: str,
        *,
        status_code: int,
        error_code: str,
        details: dict[str, Any] | None = None,
    ) -> None:
        """
        Initialize the application exception.

        Args:
            message: Human-readable error message.
            status_code: HTTP status code.
            error_code: Machine-readable error code.
            details: Optional additional error details.
        """
        super().__init__(message)

        self.message = message
        self.status_code = status_code
        self.error_code = error_code
        self.details = details or {}

    def to_dict(self) -> dict[str, Any]:
        """
        Convert the exception into a serializable dictionary.

        Returns:
            Dictionary representation of the exception.
        """
        return {
            "code": self.error_code,
            "message": self.message,
            "details": self.details,
        }

    def __str__(self) -> str:
        """
        Return the human-readable error message.
        """
        return self.message