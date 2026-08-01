"""
Security Constants.

This module centralizes reusable security-related constants used across the
application.

NOTE:
    Configuration values such as JWT secrets, API keys, algorithms, token
    expiration loaded from environment variables, etc., belong in
    app.core.config and NOT in this module.
"""

from __future__ import annotations

# ============================================================================
# AUTHENTICATION
# ============================================================================

AUTH_SCHEME_BEARER = "Bearer"
AUTHORIZATION_HEADER = "Authorization"

# ============================================================================
# TOKEN TYPES
# ============================================================================

ACCESS_TOKEN = "access"
REFRESH_TOKEN = "refresh"

# ============================================================================
# PASSWORD VALIDATION
# ============================================================================

PASSWORD_MIN_LENGTH = 8
PASSWORD_MAX_LENGTH = 128

# ============================================================================
# USERNAME VALIDATION
# ============================================================================

USERNAME_MIN_LENGTH = 3
USERNAME_MAX_LENGTH = 64

# ============================================================================
# EMAIL VALIDATION
# ============================================================================

EMAIL_MAX_LENGTH = 255

# ============================================================================
# COMMON SECURITY HEADERS
# ============================================================================

HEADER_X_API_KEY = "X-API-Key"
HEADER_X_FORWARDED_FOR = "X-Forwarded-For"
HEADER_X_REAL_IP = "X-Real-IP"

# ============================================================================
# MIME TYPES
# ============================================================================

CONTENT_TYPE_JSON = "application/json"

# ============================================================================
# HASHING
# ============================================================================

DEFAULT_PASSWORD_HASH_SCHEME = "bcrypt"

# ============================================================================
# LOGIN / AUTH LIMITS
# ============================================================================

MAX_LOGIN_ATTEMPTS = 5

# ============================================================================
# EXPORTS
# ============================================================================

__all__ = [
    # Authentication
    "AUTH_SCHEME_BEARER",
    "AUTHORIZATION_HEADER",

    # Token types
    "ACCESS_TOKEN",
    "REFRESH_TOKEN",

    # Password validation
    "PASSWORD_MIN_LENGTH",
    "PASSWORD_MAX_LENGTH",

    # Username validation
    "USERNAME_MIN_LENGTH",
    "USERNAME_MAX_LENGTH",

    # Email validation
    "EMAIL_MAX_LENGTH",

    # Headers
    "HEADER_X_API_KEY",
    "HEADER_X_FORWARDED_FOR",
    "HEADER_X_REAL_IP",

    # MIME types
    "CONTENT_TYPE_JSON",

    # Hashing
    "DEFAULT_PASSWORD_HASH_SCHEME",

    # Limits
    "MAX_LOGIN_ATTEMPTS",
]