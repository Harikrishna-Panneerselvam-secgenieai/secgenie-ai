import pytest

from app.utils.validators import (
    validate_cve,
    validate_email,
    validate_hostname,
    validate_ip,
    validate_mitre_id,
    validate_timestamp,
    validate_url,
    validate_uuid,
)

# =============================================================================
# UUID Validation
# =============================================================================

def test_validate_uuid_valid():
    assert validate_uuid("550e8400-e29b-41d4-a716-446655440000") is True


def test_validate_uuid_invalid():
    with pytest.raises(ValueError):
        validate_uuid("invalid-uuid")


# =============================================================================
# IP Address Validation
# =============================================================================

def test_validate_ipv4():
    assert validate_ip("192.168.1.10") is True


def test_validate_ipv6():
    assert validate_ip("2001:db8::1") is True


def test_validate_invalid_ip():
    with pytest.raises(ValueError):
        validate_ip("999.999.999.999")


# =============================================================================
# Email Validation
# =============================================================================

def test_validate_email_valid():
    assert validate_email("admin@example.com") is True


def test_validate_email_invalid():
    with pytest.raises(ValueError):
        validate_email("admin@")


# =============================================================================
# URL Validation
# =============================================================================

def test_validate_url_valid():
    assert validate_url("https://example.com") is True


def test_validate_url_invalid():
    with pytest.raises(ValueError):
        validate_url("ftp://example.com")


# =============================================================================
# CVE Validation
# =============================================================================

def test_validate_cve_valid():
    assert validate_cve("CVE-2025-12345") is True


def test_validate_cve_invalid():
    with pytest.raises(ValueError):
        validate_cve("CVE12345")


# =============================================================================
# MITRE Validation
# =============================================================================

def test_validate_mitre_attack_valid():
    assert validate_mitre_id("T1059") is True


def test_validate_mitre_tactic_valid():
    assert validate_mitre_id("TA0001") is True


def test_validate_mitre_subtechnique_valid():
    assert validate_mitre_id("T1059.001") is True


def test_validate_mitre_invalid():
    with pytest.raises(ValueError):
        validate_mitre_id("ABC123")


# =============================================================================
# Hostname Validation
# =============================================================================

def test_validate_hostname_valid():
    assert validate_hostname("server01.company.local") is True


def test_validate_hostname_invalid():
    with pytest.raises(ValueError):
        validate_hostname("server@01")


# =============================================================================
# Timestamp Validation
# =============================================================================

def test_validate_timestamp_valid():
    assert validate_timestamp("2026-07-30T12:00:00Z") is True


def test_validate_timestamp_invalid():
    with pytest.raises(ValueError):
        validate_timestamp("30/07/2026")