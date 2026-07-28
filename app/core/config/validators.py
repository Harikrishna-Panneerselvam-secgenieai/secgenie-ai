from .settings import Settings


def validate_settings(settings: Settings) -> None:
    """
    Validate application configuration during startup.
    """

    errors = []

    # Production JWT validation
    if settings.app.environment == "production":
        if not settings.jwt.secret_key:
            errors.append(
                "JWT secret key must be configured in production"
            )

    # Database validation
    if settings.database.port <= 0:
        errors.append(
            "Database port must be greater than zero"
        )

    # Redis validation
    if settings.redis.port <= 0:
        errors.append(
            "Redis port must be greater than zero"
        )

    # LLM validation
    if not settings.llm.provider:
        errors.append(
            "LLM provider must be configured"
        )

    if errors:
        raise ValueError(
            "Invalid configuration:\n"
            + "\n".join(errors)
        )