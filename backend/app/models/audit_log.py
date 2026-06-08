from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime

from app.database.base import Base


class AuditLog(Base):

    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True)

    action = Column(String(255))

    resource_type = Column(String(100))

    resource_id = Column(Integer)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )