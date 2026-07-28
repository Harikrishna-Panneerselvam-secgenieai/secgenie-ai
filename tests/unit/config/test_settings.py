from app.core.config import settings


def test_settings_load():
    assert settings.app.app_name == "SecGenie AI"
    assert settings.database.port == 5432
    assert settings.redis.port == 6379
    assert settings.llm.provider == "openai"