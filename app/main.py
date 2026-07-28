"""
SecGenie.ai Application Entry Point
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1 import router as api_router
from app.core.config import settings
from app.core.config.validators import validate_settings
from app.core.exceptions import register_exception_handlers
from app.core.middleware import register_middleware
from app.core.logging import setup_logging, get_logger


# Create module logger
logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(application: FastAPI):
    """
    Application startup and shutdown lifecycle.
    """

    # Startup
    logger.info("Starting SecGenie.ai application")

    # Validate application configuration
    validate_settings(settings)

    logger.info("Application configuration validation completed")


    # Future startup initialization:
    #
    # - Initialize database connection pool
    # - Initialize Redis connection
    # - Load LLM providers
    # - Initialize vector database
    # - Register AI agents
    # - Initialize background workers


    yield


    # Shutdown
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

    # Initialize logging first
    setup_logging()

    logger.info("Creating FastAPI application instance")


    application = FastAPI(
        title="SecGenie.ai",
        description="AI Powered Multi-Agent Cybersecurity Investigation Platform",
        version="0.1.0",
        lifespan=lifespan,
    )


    # Register middleware
    register_middleware(application)


    # Register global exception handlers
    register_exception_handlers(application)


    # Register API routes
    application.include_router(
        api_router,
        prefix="/api/v1",
    )


    @application.get("/")
    async def root():
        """
        Application root endpoint.
        """

        return {
            "application": "SecGenie.ai",
            "status": "running",
            "version": "0.1.0",
        }


    @application.get("/health")
    async def health():
        """
        Application health check endpoint.
        """

        return {
            "status": "healthy",
        }


    logger.info("FastAPI application created successfully")

    return application


# Application entry point
app = create_app()