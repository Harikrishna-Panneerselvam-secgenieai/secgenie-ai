"""
Agent Constants.

This module centralizes reusable constants shared by all AI agents within
the SecGenie platform.

These constants are intentionally framework-independent and can be used by
base agents, orchestrators, planners, task executors, and future agent
implementations.

NOTE:
    - Agent implementations should define their own business logic.
    - Provider-specific configuration belongs in app.core.config.
"""

from __future__ import annotations

# ============================================================================
# AGENT EXECUTION DEFAULTS
# ============================================================================

DEFAULT_AGENT_TIMEOUT_SECONDS = 300
DEFAULT_AGENT_MAX_RETRIES = 3
DEFAULT_AGENT_RETRY_DELAY_SECONDS = 5

# ============================================================================
# CONCURRENCY
# ============================================================================

DEFAULT_MAX_PARALLEL_AGENTS = 5
DEFAULT_MAX_CONCURRENT_TASKS = 10

# ============================================================================
# EXECUTION LIMITS
# ============================================================================

DEFAULT_TASK_QUEUE_SIZE = 100
DEFAULT_TASK_BATCH_SIZE = 25

# ============================================================================
# AGENT CACHE PREFIXES
# ============================================================================

CACHE_AGENT = "agent"
CACHE_AGENT_RESULT = "agent_result"
CACHE_AGENT_CONTEXT = "agent_context"
CACHE_AGENT_TASK = "agent_task"

# ============================================================================
# EXECUTION METADATA KEYS
# ============================================================================

METADATA_AGENT_NAME = "agent_name"
METADATA_AGENT_TYPE = "agent_type"
METADATA_TASK_ID = "task_id"
METADATA_INVESTIGATION_ID = "investigation_id"
METADATA_EXECUTION_ID = "execution_id"
METADATA_STARTED_AT = "started_at"
METADATA_COMPLETED_AT = "completed_at"
METADATA_DURATION = "duration"

# ============================================================================
# CONTEXT KEYS
# ============================================================================

CONTEXT_INVESTIGATION = "investigation"
CONTEXT_FINDINGS = "findings"
CONTEXT_EVIDENCE = "evidence"
CONTEXT_TIMELINE = "timeline"
CONTEXT_METADATA = "metadata"

# ============================================================================
# RESULT KEYS
# ============================================================================

RESULT_STATUS = "status"
RESULT_MESSAGE = "message"
RESULT_DATA = "data"
RESULT_ERRORS = "errors"
RESULT_WARNINGS = "warnings"

# ============================================================================
# DEFAULT TAGS
# ============================================================================

TAG_AGENT = "agent"
TAG_INVESTIGATION = "investigation"
TAG_EXECUTION = "execution"

# ============================================================================
# EXPORTS
# ============================================================================

__all__ = [
    # Execution defaults
    "DEFAULT_AGENT_TIMEOUT_SECONDS",
    "DEFAULT_AGENT_MAX_RETRIES",
    "DEFAULT_AGENT_RETRY_DELAY_SECONDS",
    # Concurrency
    "DEFAULT_MAX_PARALLEL_AGENTS",
    "DEFAULT_MAX_CONCURRENT_TASKS",
    # Limits
    "DEFAULT_TASK_QUEUE_SIZE",
    "DEFAULT_TASK_BATCH_SIZE",
    # Cache
    "CACHE_AGENT",
    "CACHE_AGENT_RESULT",
    "CACHE_AGENT_CONTEXT",
    "CACHE_AGENT_TASK",
    # Metadata
    "METADATA_AGENT_NAME",
    "METADATA_AGENT_TYPE",
    "METADATA_TASK_ID",
    "METADATA_INVESTIGATION_ID",
    "METADATA_EXECUTION_ID",
    "METADATA_STARTED_AT",
    "METADATA_COMPLETED_AT",
    "METADATA_DURATION",
    # Context
    "CONTEXT_INVESTIGATION",
    "CONTEXT_FINDINGS",
    "CONTEXT_EVIDENCE",
    "CONTEXT_TIMELINE",
    "CONTEXT_METADATA",
    # Result
    "RESULT_STATUS",
    "RESULT_MESSAGE",
    "RESULT_DATA",
    "RESULT_ERRORS",
    "RESULT_WARNINGS",
    # Tags
    "TAG_AGENT",
    "TAG_INVESTIGATION",
    "TAG_EXECUTION",
]
