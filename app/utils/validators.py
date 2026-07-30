"""
Common validation utilities for the SecGenie AI platform.

This module provides reusable validation functions that can be used across
API routes, services, agents, repositories, and schemas.

The validators are intentionally framework-independent and rely only on
Python's standard library.
"""

from __future__ import annotations

import ipaddress
import re
import uuid
from datetime import datetime
from urllib.parse import urlparse


# =============================================================================
# Regular Expressions
# =============================================================================

EMAIL_REGEX = re.compile(
    r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
)

CVE_REGEX = re.compile(
    r"^CVE-\d{4}-\d{4,}$",
    re.IGNORECASE,
)

# Examples:
# TA0001
# T1059
# T1059.001
MITRE_REGEX = re.compile(
    r"^(TA\d{4}|T\d{4}(?:\.\d{3})?)$",
    re.IGNORECASE,
)

HOSTNAME_REGEX = re.compile(
    r"^(?=.{1,253}$)(?!-)[A-Za-z0-9-]{1,63}"
    r"(?<!-)(?:\.(?!-)[A-Za-z0-9-]{1,63}(?<!-))*\.?$"
)


# =============================================================================
# UUID
# =============================================================================

def validate_uuid(value: str) -> bool:
    """
    Validate a UUID string.

    Args:
        value: UUID string.

    Returns:
        True if valid.

    Raises:
        ValueError: If invalid.
    """
    try:
        uuid.UUID(str(value))
        return True
    except (ValueError, TypeError):
        raise ValueError(f"Invalid UUID: {value}")


# =============================================================================
# IP Address
# =============================================================================

def validate_ip(value: str) -> bool:
    """
    Validate IPv4 or IPv6 address.
    """
    try:
        ipaddress.ip_address(value)
        return True
    except ValueError:
        raise ValueError(f"Invalid IP address: {value}")


# =============================================================================
# Email
# =============================================================================

def validate_email(value: str) -> bool:
    """
    Validate an email address.
    """
    if not EMAIL_REGEX.fullmatch(value):
        raise ValueError(f"Invalid email address: {value}")

    return True


# =============================================================================
# URL
# =============================================================================

def validate_url(value: str) -> bool:
    """
    Validate HTTP or HTTPS URL.
    """
    parsed = urlparse(value)

    if parsed.scheme not in ("http", "https"):
        raise ValueError("URL must use HTTP or HTTPS.")

    if not parsed.netloc:
        raise ValueError("Invalid URL.")

    return True


# =============================================================================
# CVE
# =============================================================================

def validate_cve(value: str) -> bool:
    """
    Validate a CVE identifier.

    Examples:
        CVE-2025-1234
        CVE-2024-99999
    """
    if not CVE_REGEX.fullmatch(value):
        raise ValueError(f"Invalid CVE ID: {value}")

    return True


# =============================================================================
# MITRE ATT&CK
# =============================================================================

def validate_mitre_id(value: str) -> bool:
    """
    Validate MITRE ATT&CK IDs.

    Supported:
        TA0001
        T1059
        T1059.001
    """
    if not MITRE_REGEX.fullmatch(value):
        raise ValueError(f"Invalid MITRE ATT&CK ID: {value}")

    return True


# =============================================================================
# Hostname
# =============================================================================

def validate_hostname(value: str) -> bool:
    """
    Validate hostname or FQDN.
    """
    if not HOSTNAME_REGEX.fullmatch(value):
        raise ValueError(f"Invalid hostname: {value}")

    return True


# =============================================================================
# Timestamp
# =============================================================================

def validate_timestamp(value: str) -> bool:
    """
    Validate an ISO-8601 timestamp.

    Supports:
        2026-07-30T10:30:00
        2026-07-30T10:30:00Z
        2026-07-30T10:30:00+05:30
    """
    try:
        if value.endswith("Z"):
            value = value[:-1] + "+00:00"

        datetime.fromisoformat(value)

        return True

    except ValueError:
        raise ValueError(f"Invalid ISO-8601 timestamp: {value}")