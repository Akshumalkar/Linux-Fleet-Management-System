from fastapi import APIRouter

router = APIRouter()
from app.api.health import router as health_router

app.include_router(health_router)
@router.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "fleet-management"
    }