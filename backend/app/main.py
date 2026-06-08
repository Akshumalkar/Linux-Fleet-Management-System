from fastapi import FastAPI

from app.database.base import Base
from app.database.database import engine

# Import models
from app.models.user import User
from app.models.server import Server
from app.models.alert import Alert
from app.models.audit_log import AuditLog

# Import routers
from app.api.auth import router as auth_router

# Create app FIRST
app = FastAPI(
    title="Linux Fleet Management Platform"
)

# Register routers AFTER app is created
app.include_router(auth_router)

# Create tables on startup
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {
        "message": "Linux Fleet Management Platform"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }