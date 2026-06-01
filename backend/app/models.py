from sqlalchemy import Column, Integer, String
from app.database import Base


class Node(Base):
    __tablename__ = "nodes"

    id = Column(Integer, primary_key=True, index=True)

    hostname = Column(String, unique=True, index=True)

    ip_address = Column(String, unique=True)

    ssh_username = Column(String)

    ssh_password = Column(String)

    ssh_port = Column(Integer, default=22)

    status = Column(String)