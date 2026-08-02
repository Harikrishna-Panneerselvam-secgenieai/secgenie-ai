"""
Logging identifier generation utilities.
"""

from __future__ import annotations

from uuid import uuid4


def generate_request_id() -> str:
    """
    Generate a unique request identifier.
    """
    return f"req_{uuid4().hex}"


def generate_correlation_id() -> str:
    """
    Generate a unique correlation identifier.
    """
    return f"corr_{uuid4().hex}"


def generate_execution_id() -> str:
    """
    Generate a unique execution identifier.
    """
    return f"exec_{uuid4().hex}"
