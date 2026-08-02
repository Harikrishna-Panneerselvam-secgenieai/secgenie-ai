"""
API Constants.

This module centralizes reusable API-related constants to eliminate
hardcoded values across routers, middleware, services, and schemas.

Categories:
    - API routes
    - API versioning
    - Pagination defaults
    - Request/Response headers
    - Content types
    - HTTP methods
    - Timeouts
"""

from __future__ import annotations

# ============================================================================
# API VERSIONING
# ============================================================================

API_VERSION = "v1"
API_PREFIX = f"/api/{API_VERSION}"

# ============================================================================
# PAGINATION DEFAULTS
# ============================================================================

DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100
MIN_PAGE_SIZE = 1

# ============================================================================
# DEFAULT API SETTINGS
# ============================================================================

DEFAULT_REQUEST_TIMEOUT = 30  # seconds

# ============================================================================
# HTTP HEADER NAMES
# ============================================================================

HEADER_REQUEST_ID = "X-Request-ID"
HEADER_CORRELATION_ID = "X-Correlation-ID"
HEADER_EXECUTION_ID = "X-Execution-ID"

HEADER_AUTHORIZATION = "Authorization"
HEADER_CONTENT_TYPE = "Content-Type"
HEADER_ACCEPT = "Accept"

# ============================================================================
# CONTENT TYPES
# ============================================================================

CONTENT_TYPE_JSON = "application/json"
CONTENT_TYPE_TEXT = "text/plain"
CONTENT_TYPE_HTML = "text/html"
CONTENT_TYPE_OCTET_STREAM = "application/octet-stream"

# ============================================================================
# HTTP METHODS
# ============================================================================

HTTP_GET = "GET"
HTTP_POST = "POST"
HTTP_PUT = "PUT"
HTTP_PATCH = "PATCH"
HTTP_DELETE = "DELETE"

# ============================================================================
# COMMON API ROUTES
# ============================================================================

HEALTH_ENDPOINT = "/health"
METRICS_ENDPOINT = "/metrics"
DOCS_ENDPOINT = "/docs"
OPENAPI_ENDPOINT = "/openapi.json"

# ============================================================================
# EXPORTS
# ============================================================================

__all__ = [
    # Versioning
    "API_VERSION",
    "API_PREFIX",
    # Pagination
    "DEFAULT_PAGE",
    "DEFAULT_PAGE_SIZE",
    "MAX_PAGE_SIZE",
    "MIN_PAGE_SIZE",
    # Defaults
    "DEFAULT_REQUEST_TIMEOUT",
    # Headers
    "HEADER_REQUEST_ID",
    "HEADER_CORRELATION_ID",
    "HEADER_EXECUTION_ID",
    "HEADER_AUTHORIZATION",
    "HEADER_CONTENT_TYPE",
    "HEADER_ACCEPT",
    # Content Types
    "CONTENT_TYPE_JSON",
    "CONTENT_TYPE_TEXT",
    "CONTENT_TYPE_HTML",
    "CONTENT_TYPE_OCTET_STREAM",
    # HTTP Methods
    "HTTP_GET",
    "HTTP_POST",
    "HTTP_PUT",
    "HTTP_PATCH",
    "HTTP_DELETE",
    # Routes
    "HEALTH_ENDPOINT",
    "METRICS_ENDPOINT",
    "DOCS_ENDPOINT",
    "OPENAPI_ENDPOINT",
]
