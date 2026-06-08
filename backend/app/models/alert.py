from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime

from app.database.base import Base


class Alert(Base):

    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True)

    severity = Column(String(20))

    message = Column(String(500))

    status = Column(String(50))

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )