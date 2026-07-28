"""
SecGenie.ai Application Entry Point
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1 import router as api_router
from app.core.config import settings
from app.core.config.validators import validate_settings
from app.core.middleware import register_middleware
from app.core.exceptions import register_exception_handlers


@asynccontextmanager
async def lifespan(application: FastAPI):
    """
    Application startup and shutdown lifecycle.
    """

    # Startup validation
    validate_settings(settings)

    # Future startup tasks:
    # - Initialize database connection pool
    # - Initialize Redis
    # - Load AI providers
    # - Register agents

    yield

    # Shutdown logic:
    # - Close database connections
    # - Close Redis connections
    # - Stop background workers
    # - Cleanup resources


def create_app() -> FastAPI:
    """
    Application factory.

    Creates and configures the FastAPI application.
    """

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
        return {
            "application": "SecGenie.ai",
            "status": "running",
            "version": "0.1.0",
        }


    @application.get("/health")
    async def health():
        return {
            "status": "healthy",
        }


    return application


app = create_app()