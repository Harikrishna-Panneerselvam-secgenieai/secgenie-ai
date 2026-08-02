"""
Database Constants.

This module centralizes reusable database-related constants used across
repositories, services, migrations, and database utilities.

NOTE:
    Environment-specific values (host, port, username, password, URL, etc.)
    belong in the configuration module (app.core.config), NOT here.
"""

from __future__ import annotations

# ============================================================================
# DATABASE DEFAULTS
# ============================================================================

DEFAULT_BATCH_SIZE = 100
DEFAULT_FETCH_SIZE = 100
DEFAULT_QUERY_TIMEOUT = 30  # seconds

# ============================================================================
# CONNECTION POOL DEFAULTS
# ============================================================================

DEFAULT_POOL_SIZE = 20
DEFAULT_MAX_OVERFLOW = 10
DEFAULT_POOL_TIMEOUT = 30  # seconds
DEFAULT_POOL_RECYCLE = 1800  # seconds (30 minutes)

# ============================================================================
# PAGINATION LIMITS
# ============================================================================

DEFAULT_OFFSET = 0
DEFAULT_LIMIT = 20
MAX_LIMIT = 100

# ============================================================================
# TRANSACTION SETTINGS
# ============================================================================

DEFAULT_TRANSACTION_RETRIES = 3
DEFAULT_RETRY_DELAY_SECONDS = 1

# ============================================================================
# SOFT DELETE
# ============================================================================

SOFT_DELETE_FIELD = "deleted_at"

# ============================================================================
# TIMESTAMP FIELD NAMES
# ============================================================================

CREATED_AT_FIELD = "created_at"
UPDATED_AT_FIELD = "updated_at"

# ============================================================================
# PRIMARY KEY
# ============================================================================

PRIMARY_KEY_FIELD = "id"

# ============================================================================
# COMMON DATABASE COLUMN LENGTHS
# ============================================================================

UUID_LENGTH = 36
EMAIL_MAX_LENGTH = 255
NAME_MAX_LENGTH = 255
TITLE_MAX_LENGTH = 255
DESCRIPTION_MAX_LENGTH = 5000

# ============================================================================
# EXPORTS
# ============================================================================

__all__ = [
    # Database defaults
    "DEFAULT_BATCH_SIZE",
    "DEFAULT_FETCH_SIZE",
    "DEFAULT_QUERY_TIMEOUT",
    # Connection pool
    "DEFAULT_POOL_SIZE",
    "DEFAULT_MAX_OVERFLOW",
    "DEFAULT_POOL_TIMEOUT",
    "DEFAULT_POOL_RECYCLE",
    # Pagination
    "DEFAULT_OFFSET",
    "DEFAULT_LIMIT",
    "MAX_LIMIT",
    # Transactions
    "DEFAULT_TRANSACTION_RETRIES",
    "DEFAULT_RETRY_DELAY_SECONDS",
    # Soft delete
    "SOFT_DELETE_FIELD",
    # Timestamp fields
    "CREATED_AT_FIELD",
    "UPDATED_AT_FIELD",
    # Primary key
    "PRIMARY_KEY_FIELD",
    # Lengths
    "UUID_LENGTH",
    "EMAIL_MAX_LENGTH",
    "NAME_MAX_LENGTH",
    "TITLE_MAX_LENGTH",
    "DESCRIPTION_MAX_LENGTH",
]
