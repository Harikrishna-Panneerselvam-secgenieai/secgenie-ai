"""
Investigation status enumeration.

Defines the lifecycle states for an investigation.
"""

from enum import Enum


class InvestigationStatus(str, Enum):
    """Lifecycle states for an investigation."""

    CREATED = "CREATED"
    QUEUED = "QUEUED"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"
