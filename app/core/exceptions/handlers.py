"""
Global exception handlers for SecGenie.ai.

This module registers centralized exception handlers for the FastAPI
application. All exceptions are converted into a standard API response
format and logged using the application's structured logging system.
"""

from __future__ import annotations

from typing import Any

from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.core.exceptions.base import AppException
from app.core.logging import get_logger
from app.schemas.error_response import (
    ErrorDetail,
    ErrorResponse,
)

logger = get_logger(__name__)


def _build_error_response(
    request: Request,
    *,
    code: str,
    message: str,
    status_code: int,
    details: dict[str, Any] | None = None,
) -> JSONResponse:
    """
    Build the standard error response.
    """

    response = ErrorResponse(
        error=ErrorDetail(
            code=code,
            message=message,
            details=details or {},
            request_id=getattr(request.state, "request_id", None),
            correlation_id=getattr(request.state, "correlation_id", None),
        )
    )

    return JSONResponse(
        status_code=status_code,
        content=response.model_dump(),
    )


def register_exception_handlers(app: FastAPI) -> None:
    """
    Register all global exception handlers.
    """

    @app.exception_handler(AppException)
    async def app_exception_handler(
        request: Request,
        exc: AppException,
    ) -> JSONResponse:
        """
        Handle application exceptions.
        """

        logger.warning(
            "Application exception",
            extra={
                "path": request.url.path,
                "method": request.method,
                "status_code": exc.status_code,
                "error_code": exc.error_code,
                "request_id": getattr(request.state, "request_id", None),
                "correlation_id": getattr(
                    request.state,
                    "correlation_id",
                    None,
                ),
            },
        )

        return _build_error_response(
            request,
            code=exc.error_code,
            message=exc.message,
            status_code=exc.status_code,
            details=exc.details,
        )

    @app.exception_handler(HTTPException)
    async def http_exception_handler(
        request: Request,
        exc: HTTPException,
    ) -> JSONResponse:
        """
        Handle FastAPI HTTP exceptions.
        """

        logger.warning(
            "HTTP exception",
            extra={
                "path": request.url.path,
                "method": request.method,
                "status_code": exc.status_code,
                "request_id": getattr(request.state, "request_id", None),
                "correlation_id": getattr(
                    request.state,
                    "correlation_id",
                    None,
                ),
            },
        )

        return _build_error_response(
            request,
            code="HTTP_EXCEPTION",
            message=str(exc.detail),
            status_code=exc.status_code,
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request,
        exc: RequestValidationError,
    ) -> JSONResponse:
        """
        Handle request validation errors.
        """

        logger.warning(
            "Request validation failed",
            extra={
                "path": request.url.path,
                "method": request.method,
                "errors": exc.errors(),
                "request_id": getattr(request.state, "request_id", None),
                "correlation_id": getattr(
                    request.state,
                    "correlation_id",
                    None,
                ),
            },
        )

        return _build_error_response(
            request,
            code="VALIDATION_ERROR",
            message="Request validation failed.",
            status_code=422,
            details={
                "errors": exc.errors(),
            },
        )

    @app.exception_handler(Exception)
    async def global_exception_handler(
        request: Request,
        exc: Exception,
    ) -> JSONResponse:
        """
        Handle all unexpected exceptions.
        """

        logger.exception(
            "Unhandled exception",
            extra={
                "path": request.url.path,
                "method": request.method,
                "request_id": getattr(request.state, "request_id", None),
                "correlation_id": getattr(
                    request.state,
                    "correlation_id",
                    None,
                ),
            },
        )

        return _build_error_response(
            request,
            code="INTERNAL_SERVER_ERROR",
            message="An unexpected error occurred.",
            status_code=500,
        )
