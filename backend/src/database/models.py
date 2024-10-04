import enum
from datetime import datetime
from typing import Any

from sqlalchemy import TIMESTAMP, Column, String
from sqlalchemy.dialects.postgresql import ENUM as PgEnum

from .db import Base


class Role(enum.Enum):
    user = "user"
    recruiter = "recruiter"
    director = "director"
    admin = "admin"


class User(Base):
    __tablename__ = "users"
    username = Column(String, nullable=False, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, default=0)
    role = Column(
        PgEnum(Role, name="user_role", create_type=False),
        nullable=False,
        default=Role.user,
    )
    hashed_password = Column(String, nullable=False)
    refresh_token = Column(String, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, unique=False, default=datetime.now)

    def to_dict(self) -> dict[str, Any]:
        return {
            "username": self.username,
            "name": self.name,
            "email": self.email,
            "role": self.role,
            "hashed_password": self.hashed_password,
            "refresh_token": self.refresh_token,
            "created_at": self.created_at,
        }
