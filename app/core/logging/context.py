"""
Logging context management.

This module provides async-safe context storage for structured logging.
Values stored here are automatically isolated per request/coroutine using
Python's contextvars module.
"""

from __future__ import annotations

from contextvars import ContextVar

# Context variables
_request_id: ContextVar[str | None] = ContextVar(
    "request_id",
    default=None,
)

_correlation_id: ContextVar[str | None] = ContextVar(
    "correlation_id",
    default=None,
)

_execution_id: ContextVar[str | None] = ContextVar(
    "execution_id",
    default=None,
)


# --------------------------------------------------------------------------
# Request ID
# --------------------------------------------------------------------------


def set_request_id(request_id: str) -> None:
    """Store the current request ID."""
    _request_id.set(request_id)


def get_request_id() -> str | None:
    """Return the current request ID."""
    return _request_id.get()


def clear_request_id() -> None:
    """Clear the current request ID."""
    _request_id.set(None)


# --------------------------------------------------------------------------
# Correlation ID
# --------------------------------------------------------------------------


def set_correlation_id(correlation_id: str) -> None:
    """Store the current correlation ID."""
    _correlation_id.set(correlation_id)


def get_correlation_id() -> str | None:
    """Return the current correlation ID."""
    return _correlation_id.get()


def clear_correlation_id() -> None:
    """Clear the current correlation ID."""
    _correlation_id.set(None)


# --------------------------------------------------------------------------
# Execution ID
# --------------------------------------------------------------------------


def set_execution_id(execution_id: str) -> None:
    """Store the current execution ID."""
    _execution_id.set(execution_id)


def get_execution_id() -> str | None:
    """Return the current execution ID."""
    return _execution_id.get()


def clear_execution_id() -> None:
    """Clear the current execution ID."""
    _execution_id.set(None)


# --------------------------------------------------------------------------
# Utilities
# --------------------------------------------------------------------------


def clear_context() -> None:
    """
    Clear all logging context values.

    This should typically be called at the end of each request to prevent
    context leakage between requests.
    """
    clear_request_id()
    clear_correlation_id()
    clear_execution_id()
