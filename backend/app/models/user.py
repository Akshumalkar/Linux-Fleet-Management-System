from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime

from app.database.base import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    name = Column(String(100))

    email = Column(String(255), unique=True)

    password_hash = Column(String(255))

    role = Column(String(50))

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )