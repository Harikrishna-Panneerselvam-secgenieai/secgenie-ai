from fastapi import APIRouter

from app.api.v1.investigations.router import router as investigations_router


router = APIRouter()


router.include_router(
    investigations_router,
)
