from fastapi import APIRouter


router = APIRouter(
    prefix="/investigations",
    tags=["Investigations"]
)


@router.get("/")
async def get_investigations():
    return {
        "module": "investigations",
        "status": "ready"
    }
