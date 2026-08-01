"""
Investigation Constants.

This module centralizes reusable investigation-related constants used across
the domain layer, services, repositories, schemas, and AI agents.

NOTE:
    Investigation statuses, priorities, and lifecycle transitions should be
    implemented as Enums in the domain layer, NOT as constants.
"""

from __future__ import annotations

# ============================================================================
# INVESTIGATION VALIDATION
# ============================================================================

MIN_TITLE_LENGTH = 5
MAX_TITLE_LENGTH = 255

MIN_DESCRIPTION_LENGTH = 10
MAX_DESCRIPTION_LENGTH = 5000

# ============================================================================
# DEFAULT INVESTIGATION VALUES
# ============================================================================

DEFAULT_PRIORITY = "medium"
DEFAULT_MAX_RETRIES = 3
DEFAULT_TIMEOUT_SECONDS = 300

# ============================================================================
# PAGINATION
# ============================================================================

DEFAULT_FINDINGS_PAGE_SIZE = 50
DEFAULT_EVIDENCE_PAGE_SIZE = 50
DEFAULT_TIMELINE_PAGE_SIZE = 100

# ============================================================================
# CACHE KEY PREFIXES
# ============================================================================

CACHE_INVESTIGATION = "investigation"
CACHE_FINDINGS = "findings"
CACHE_EVIDENCE = "evidence"
CACHE_TIMELINE = "timeline"
CACHE_STATISTICS = "statistics"

# ============================================================================
# ENTITY NAMES
# ============================================================================

ENTITY_INVESTIGATION = "investigation"
ENTITY_FINDING = "finding"
ENTITY_EVIDENCE = "evidence"
ENTITY_TIMELINE = "timeline"
ENTITY_TASK = "task"
ENTITY_AUDIT_LOG = "audit_log"

# ============================================================================
# SORT FIELDS
# ============================================================================

SORT_CREATED_AT = "created_at"
SORT_UPDATED_AT = "updated_at"
SORT_PRIORITY = "priority"
SORT_STATUS = "status"

# ============================================================================
# DEFAULT SORTING
# ============================================================================

DEFAULT_SORT_FIELD = SORT_CREATED_AT
DEFAULT_SORT_ORDER = "desc"

# ============================================================================
# EXPORTS
# ============================================================================

__all__ = [
    # Validation
    "MIN_TITLE_LENGTH",
    "MAX_TITLE_LENGTH",
    "MIN_DESCRIPTION_LENGTH",
    "MAX_DESCRIPTION_LENGTH",

    # Defaults
    "DEFAULT_PRIORITY",
    "DEFAULT_MAX_RETRIES",
    "DEFAULT_TIMEOUT_SECONDS",

    # Pagination
    "DEFAULT_FINDINGS_PAGE_SIZE",
    "DEFAULT_EVIDENCE_PAGE_SIZE",
    "DEFAULT_TIMELINE_PAGE_SIZE",

    # Cache
    "CACHE_INVESTIGATION",
    "CACHE_FINDINGS",
    "CACHE_EVIDENCE",
    "CACHE_TIMELINE",
    "CACHE_STATISTICS",

    # Entities
    "ENTITY_INVESTIGATION",
    "ENTITY_FINDING",
    "ENTITY_EVIDENCE",
    "ENTITY_TIMELINE",
    "ENTITY_TASK",
    "ENTITY_AUDIT_LOG",

    # Sorting
    "SORT_CREATED_AT",
    "SORT_UPDATED_AT",
    "SORT_PRIORITY",
    "SORT_STATUS",
    "DEFAULT_SORT_FIELD",
    "DEFAULT_SORT_ORDER",
]