import pytest


@pytest.fixture
def sample_user():
    return {
        "username": "test_user",
        "email": "test@example.com",
    }


@pytest.fixture
def sample_investigation():
    return {
        "title": "Failed Login Investigation",
        "description": "Repeated failed authentication attempts",
        "status": "CREATED",
    }
