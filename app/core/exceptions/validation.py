"""
Validation exception definitions for SecGenie.ai.

This module contains exceptions raised when request data
or business rules fail validation.

Examples:

- ValidationError
- InvalidInputError
"""


from __future__ import annotations

from typing import Any

from app.core.exceptions.base import AppException


class ValidationError(AppException):
    """
    Raised when business validation fails.

    Examples:
        - Investigation name already exists.
        - Asset is inactive.
        - Investigation cannot transition to the requested status.
        - Risk score is outside the allowed range.
    """

    def __init__(
        self,
        message: str = "Validation failed.",
        *,
        error_code: str = "VALIDATION_ERROR",
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(
            message=message,
            status_code=422,
            error_code=error_code,
            details=details,
        )