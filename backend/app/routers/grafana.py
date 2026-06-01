from fastapi import APIRouter
from app.services.grafana_service import create_dashboard_for_node

router = APIRouter()

@router.post("/grafana/dashboard/create")
def create_dashboard(data: dict):
    return create_dashboard_for_node(
        node_name=data["node_name"],
        instance=data["instance"]
    )