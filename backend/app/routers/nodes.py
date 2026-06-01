from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Node
from app.schemas import (
    NodeCreate,
    NodeResponse,
    CommandRequest
)
from app.services.ssh_service import execute_ssh_command

router = APIRouter()


# Database dependency
def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# GET all nodes
@router.get(
    "/nodes",
    response_model=list[NodeResponse]
)
def get_nodes(
    db: Session = Depends(get_db)
):
    return db.query(Node).all()


# CREATE node
@router.post(
    "/nodes",
    response_model=NodeResponse
)
def create_node(
    node: NodeCreate,
    db: Session = Depends(get_db)
):
    db_node = Node(
        hostname=node.hostname,
        ip_address=node.ip_address,
        ssh_username=node.ssh_username,
        ssh_password=node.ssh_password,
        ssh_port=node.ssh_port,
        status="active"
    )

    db.add(db_node)

    db.commit()

    db.refresh(db_node)

    return db_node


# EXECUTE remote command
@router.post("/nodes/{node_id}/execute")
def execute_command(
    node_id: int,
    request: CommandRequest,
    db: Session = Depends(get_db)
):
    node = db.query(Node).filter(
        Node.id == node_id
    ).first()

    if not node:
        return {
            "success": False,
            "error": "Node not found"
        }

    result = execute_ssh_command(
        hostname=node.ip_address,
        username=node.ssh_username,
        password=node.ssh_password,
        port=node.ssh_port,
        command=request.command
    )

    return result