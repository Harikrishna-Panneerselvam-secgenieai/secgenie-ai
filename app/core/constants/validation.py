"""
Validation Constants.

This module centralizes reusable validation constants shared across
Pydantic schemas, validators, services, and domain models.

NOTE:
    Model-specific validation rules should remain within the appropriate
    schema or domain model.
"""

from __future__ import annotations

# ============================================================================
# GENERIC STRING LENGTHS
# ============================================================================

MIN_NAME_LENGTH = 2
MAX_NAME_LENGTH = 255

MIN_TITLE_LENGTH = 5
MAX_TITLE_LENGTH = 255

MIN_DESCRIPTION_LENGTH = 10
MAX_DESCRIPTION_LENGTH = 5000

# ============================================================================
# USER VALIDATION
# ============================================================================

MIN_USERNAME_LENGTH = 3
MAX_USERNAME_LENGTH = 64

EMAIL_MAX_LENGTH = 255

PASSWORD_MIN_LENGTH = 8
PASSWORD_MAX_LENGTH = 128

# ============================================================================
# IDENTIFIER VALIDATION
# ============================================================================

UUID_LENGTH = 36

# ============================================================================
# PAGINATION VALIDATION
# ============================================================================

MIN_PAGE = 1
MIN_PAGE_SIZE = 1
MAX_PAGE_SIZE = 100

# ============================================================================
# COLLECTION LIMITS
# ============================================================================

MAX_TAGS = 20
MAX_ITEMS_PER_REQUEST = 100

# ============================================================================
# FILE VALIDATION
# ============================================================================

MAX_FILENAME_LENGTH = 255
MAX_FILE_SIZE_MB = 100

# ============================================================================
# REGULAR EXPRESSIONS
# ============================================================================

EMAIL_REGEX = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

USERNAME_REGEX = r"^[A-Za-z0-9_.-]+$"

# ============================================================================
# EXPORTS
# ============================================================================

__all__ = [
    # Generic strings
    "MIN_NAME_LENGTH",
    "MAX_NAME_LENGTH",
    "MIN_TITLE_LENGTH",
    "MAX_TITLE_LENGTH",
    "MIN_DESCRIPTION_LENGTH",
    "MAX_DESCRIPTION_LENGTH",
    # User
    "MIN_USERNAME_LENGTH",
    "MAX_USERNAME_LENGTH",
    "EMAIL_MAX_LENGTH",
    "PASSWORD_MIN_LENGTH",
    "PASSWORD_MAX_LENGTH",
    # Identifiers
    "UUID_LENGTH",
    # Pagination
    "MIN_PAGE",
    "MIN_PAGE_SIZE",
    "MAX_PAGE_SIZE",
    # Collections
    "MAX_TAGS",
    "MAX_ITEMS_PER_REQUEST",
    # Files
    "MAX_FILENAME_LENGTH",
    "MAX_FILE_SIZE_MB",
    # Regex
    "EMAIL_REGEX",
    "USERNAME_REGEX",
]
