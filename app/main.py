"""
SecGenie.ai Application Entry Point
"""

from fastapi import FastAPI

from app.api.v1 import router as api_router


def create_app() -> FastAPI:

    application = FastAPI(
        title="SecGenie.ai",
        description="AI Powered Multi-Agent Cybersecurity Investigation Platform",
        version="0.1.0",
    )

    # Register API routes
    application.include_router(
        api_router,
        prefix="/api/v1"
    )

    @application.get("/")
    async def root():
        return {
            "application": "SecGenie.ai",
            "status": "running",
            "version": "0.1.0"
        }

    @application.get("/health")
    async def health():
        return {
            "status": "healthy"
        }

    return application


app = create_app()
