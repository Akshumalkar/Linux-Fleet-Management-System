from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime

from app.database.base import Base


class Server(Base):

    __tablename__ = "servers"

    id = Column(Integer, primary_key=True)

    hostname = Column(String(100))

    ip_address = Column(String(50))

    operating_system = Column(String(100))

    environment = Column(String(50))

    status = Column(String(50))

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )