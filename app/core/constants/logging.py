"""
Logging Constants.

This module centralizes reusable logging constants used across the
application for structured logging, request tracing, and observability.

These constants should be used by:
    - Logging configuration
    - Middleware
    - Context variables
    - Services
    - AI agents
"""

from __future__ import annotations

from .api import (
    HEADER_CORRELATION_ID,
    HEADER_EXECUTION_ID,
    HEADER_REQUEST_ID,
)

# ============================================================================
# DEFAULT LOGGING CONFIGURATION
# ============================================================================

DEFAULT_LOG_LEVEL = "INFO"
DEFAULT_LOGGER_NAME = "secgenie"

# ============================================================================
# LOG RECORD FIELD NAMES
# ============================================================================

LOG_TIMESTAMP = "timestamp"
LOG_LEVEL = "level"
LOG_MESSAGE = "message"
LOG_LOGGER = "logger"
LOG_MODULE = "module"
LOG_FUNCTION = "function"
LOG_LINE = "line"

# ============================================================================
# REQUEST CONTEXT FIELDS
# ============================================================================

REQUEST_ID = "request_id"
CORRELATION_ID = "correlation_id"
EXECUTION_ID = "execution_id"

# ============================================================================
# TRACE CONTEXT HEADERS
# ============================================================================

# ============================================================================
# LOGGING EXTRA FIELD KEYS
# ============================================================================

EXTRA_REQUEST_ID = REQUEST_ID
EXTRA_CORRELATION_ID = CORRELATION_ID
EXTRA_EXECUTION_ID = EXECUTION_ID

# ============================================================================
# LOGGER NAMES
# ============================================================================

APP_LOGGER = "app"
API_LOGGER = "api"
DATABASE_LOGGER = "database"
SECURITY_LOGGER = "security"
AGENT_LOGGER = "agent"
AUDIT_LOGGER = "audit"

# ============================================================================
# LOG FORMAT TYPES
# ============================================================================

LOG_FORMAT_JSON = "json"
LOG_FORMAT_TEXT = "text"

# ============================================================================
# EXPORTS
# ============================================================================

__all__ = [
    # Default configuration
    "DEFAULT_LOG_LEVEL",
    "DEFAULT_LOGGER_NAME",
    # Log fields
    "LOG_TIMESTAMP",
    "LOG_LEVEL",
    "LOG_MESSAGE",
    "LOG_LOGGER",
    "LOG_MODULE",
    "LOG_FUNCTION",
    "LOG_LINE",
    # Context fields
    "REQUEST_ID",
    "CORRELATION_ID",
    "EXECUTION_ID",
    # Headers
    "HEADER_REQUEST_ID",
    "HEADER_CORRELATION_ID",
    "HEADER_EXECUTION_ID",
    # Extra keys
    "EXTRA_REQUEST_ID",
    "EXTRA_CORRELATION_ID",
    "EXTRA_EXECUTION_ID",
    # Logger names
    "APP_LOGGER",
    "API_LOGGER",
    "DATABASE_LOGGER",
    "SECURITY_LOGGER",
    "AGENT_LOGGER",
    "AUDIT_LOGGER",
    # Formats
    "LOG_FORMAT_JSON",
    "LOG_FORMAT_TEXT",
]
