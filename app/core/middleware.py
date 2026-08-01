from __future__ import annotations

import time
from collections.abc import Callable

from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.cors import CORSMiddleware

from app.core.constants.api import (
    HEADER_CORRELATION_ID,
    HEADER_REQUEST_ID,
)
from app.core.logging import get_logger
from app.core.logging.context import (
    clear_context,
    set_correlation_id,
    set_request_id,
)
from app.core.logging.id_generator import (
    generate_correlation_id,
    generate_request_id,
)

logger = get_logger(__name__)


class LoggingContextMiddleware(BaseHTTPMiddleware):
    """
    Middleware that creates and manages the logging context
    for every incoming HTTP request and measures execution time.
    """

    async def dispatch(
        self,
        request: Request,
        call_next: Callable[[Request], Response],
    ) -> Response:
        """
        Process a request, measure execution time,
        and enrich all logs with request context.
        """

        # Start measuring request duration.
        start_time = time.perf_counter()

        # Generate a unique request ID.
        request_id = generate_request_id()

        # Reuse the incoming correlation ID if provided,
        # otherwise generate a new one.
        correlation_id = request.headers.get(HEADER_CORRELATION_ID)
        if correlation_id is None:
            correlation_id = generate_correlation_id()

        # ------------------------------------------------------------------
        # Store IDs in logging context
        # ------------------------------------------------------------------
        set_request_id(request_id)
        set_correlation_id(correlation_id)

        # ------------------------------------------------------------------
        # Store IDs on request.state
        #
        # This allows exception handlers, dependencies and routes to
        # reliably access the IDs even if the logging context is cleared.
        # ------------------------------------------------------------------
        request.state.request_id = request_id
        request.state.correlation_id = correlation_id

        # Placeholder until authentication is implemented.
        user = "anonymous"

        logger.info(
            "HTTP request started",
            extra={
                "method": request.method,
                "path": request.url.path,
                "client": request.client.host if request.client else None,
                "user": user,
            },
        )

        try:
            # Process the request.
            response = await call_next(request)

            # Calculate execution time.
            duration_ms = round(
                (time.perf_counter() - start_time) * 1000,
                2,
            )

            logger.info(
                "HTTP request completed",
                extra={
                    "method": request.method,
                    "path": request.url.path,
                    "status_code": response.status_code,
                    "duration_ms": duration_ms,
                    "user": user,
                },
            )

            # Return identifiers to the client.
            response.headers[HEADER_REQUEST_ID] = request_id
            response.headers[HEADER_CORRELATION_ID] = correlation_id

            # Return execution time to the client.
            response.headers["X-Execution-Time"] = f"{duration_ms} ms"

            return response

        except Exception:
            duration_ms = round(
                (time.perf_counter() - start_time) * 1000,
                2,
            )

            logger.exception(
                "HTTP request failed",
                extra={
                    "method": request.method,
                    "path": request.url.path,
                    "duration_ms": duration_ms,
                    "user": user,
                },
            )

            raise

        finally:
            # Prevent context leakage between requests.
            clear_context()


def register_middleware(app: FastAPI) -> None:
    """
    Register all application middleware.
    """

    # Structured logging middleware.
    app.add_middleware(LoggingContextMiddleware)

    # Cross-Origin Resource Sharing (CORS).
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )