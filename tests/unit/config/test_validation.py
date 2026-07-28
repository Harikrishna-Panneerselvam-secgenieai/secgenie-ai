import pytest

from app.core.config import settings
from app.core.config.settings import Settings
from app.core.config.validators import validate_settings


def test_valid_configuration():
    """Verify valid configuration passes validation."""

    validate_settings(settings)


def test_production_requires_jwt_secret(monkeypatch):
    """Production environment must have JWT secret."""

    monkeypatch.setenv(
        "APP__ENVIRONMENT",
        "production",
    )

    monkeypatch.setenv(
        "JWT__SECRET_KEY",
        "",
    )

    production_settings = Settings()

    with pytest.raises(ValueError):
        validate_settings(production_settings)