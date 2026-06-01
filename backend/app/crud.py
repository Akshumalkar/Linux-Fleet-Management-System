from sqlalchemy.orm import Session
from app import models, schemas

def create_node(db: Session, node: schemas.NodeCreate):
    db_node = models.Node(
        hostname=node.hostname,
        ip_address=node.ip_address
    )

    db.add(db_node)
    db.commit()
    db.refresh(db_node)

    return db_node


def get_nodes(db: Session):
    return db.query(models.Node).all()