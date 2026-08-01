"""
SecGenie.ai Application Entry Point
"""

from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1 import router as api_router
from app.core.config import settings
from app.core.config.validators import validate_settings
from app.core.exceptions import register_exception_handlers
from app.core.logging import get_logger, setup_logging
from app.core.middleware import register_middleware

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(application: FastAPI):
    """
    Application startup and shutdown lifecycle.
    """

    logger.info("Starting SecGenie.ai application")

    # Validate configuration
    validate_settings(settings)

    logger.info(
        "Application configuration validation completed"
    )

    # Future startup initialization:
    #
    # - Initialize database connection pool
    # - Initialize Redis connection
    # - Load LLM providers
    # - Initialize vector database
    # - Register AI agents
    # - Initialize background workers

    yield

    logger.info("Stopping SecGenie.ai application")

    # Future shutdown cleanup:
    #
    # - Close database connections
    # - Close Redis connections
    # - Stop background workers
    # - Release external API clients


def create_app() -> FastAPI:
    """
    Application factory.

    Creates and configures the FastAPI application.
    """

    # --------------------------------------------------------------
    # Initialize logging first
    # --------------------------------------------------------------
    setup_logging()

    logger.info(
        "Creating FastAPI application instance"
    )

    application = FastAPI(
        title=settings.app.app_name,
        description=(
            "AI Powered Multi-Agent Cybersecurity "
            "Investigation Platform"
        ),
        version=settings.app.app_version,
        docs_url="/docs"
        if settings.api.docs_enabled
        else None,
        redoc_url="/redoc"
        if settings.api.redoc_enabled
        else None,
        openapi_url="/openapi.json"
        if settings.api.openapi_enabled
        else None,
        lifespan=lifespan,
    )

    # --------------------------------------------------------------
    # Register middleware
    # --------------------------------------------------------------
    register_middleware(application)

    # --------------------------------------------------------------
    # Register global exception handlers
    # --------------------------------------------------------------
    register_exception_handlers(application)

    # --------------------------------------------------------------
    # Register API routes
    # --------------------------------------------------------------
    application.include_router(
        api_router,
        prefix=settings.api.prefix,
    )

    # --------------------------------------------------------------
    # Root endpoint
    # --------------------------------------------------------------
    @application.get(
        "/",
        tags=["System"],
    )
    async def root() -> dict[str, str]:
        """
        Application root endpoint.
        """

        logger.info("Root endpoint called")

        return {
            "application": settings.app.app_name,
            "status": "running",
            "version": settings.app.app_version,
        }

    # --------------------------------------------------------------
    # Health endpoint
    # --------------------------------------------------------------
    @application.get(
        "/health",
        tags=["System"],
    )
    async def health() -> dict[str, str]:
        """
        Application health check endpoint.
        """

        logger.info("Health endpoint called")

        return {
            "status": "healthy",
        }

    logger.info(
        "FastAPI application created successfully"
    )

    return application


# ------------------------------------------------------------------
# Application entry point
# ------------------------------------------------------------------

app = create_app()