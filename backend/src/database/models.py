import enum
from datetime import datetime
from typing import Any

from sqlalchemy import TIMESTAMP, Column, String, ForeignKey, Integer, TIMESTAMP, DATE
from sqlalchemy.dialects.postgresql import ENUM as PgEnum
from sqlalchemy.orm import relationship

from .db import Base


class Role(enum.Enum):
    recruiter = "recruiter"
    director = "director"
    admin = "admin"


class User(Base):
    __tablename__ = "users"
    username = Column(String, nullable=False, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    role = Column(
        PgEnum(Role, name="user_role", create_type=False),
        nullable=False,
        default=Role.recruiter,
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


class RecruitersDirectors(Base):
    __tablename__ = "list_recruiters"

    id = Column(Integer, primary_key=True, autoincrement=True)
    director_username = Column(String, ForeignKey('users.username'), nullable=False)
    recruiter_username = Column(String, ForeignKey('users.username'), nullable=False)
  
    recruiters = relationship("User", back_populates="users")
    

class Response(Base):
    __tablename__ = "responses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    family_name = Column(String, nullable=False)
    surname = Column(String, nullable=True)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    city = Column(String, nullable=False)
    vacancy_id = Column(Integer, ForeignKey('vacancies.id'), nullable=False)
    resume_file = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, unique=False, default=datetime.now)

    vacancy = relationship("Vacancies", back_populates="requests")

    def to_dict(self) -> dict[str, Any]:
        return {
            "first_name": self.first_name,
            "family_name": self.family_name,
            "surname": self.surname,
            "phone": self.phone,
            "email": self.email,
            "city": self.city,
            "vacancy_id": self.vacancy_id,
            "resume_file": self.resume_file,
            "created_at": self.created_at
        }


class Vacancy(Base):
    __tablename__ = "vacancies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    location = Column(String, nullable=False)
    recruiter_username = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, unique=False, default=datetime.now)

    users = relationship("User", back_populates="users")

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "location": self.location,
            "recruiter_id": self.recruiter_id,
            "created_at": self.created_at
        }


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String, nullable=False)
    status = Column(String, nullable=False)
    recruiter_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, unique=False, default=datetime.now)

    users = relationship("User", back_populates="users")
    
    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "recruiter_id": self.recruiter_id,
            "created_at": self.created_at
        }


class Interview(Base):
    __tablename__ = "interviews"
    id = Column(Integer, primary_key=True, autoincrement=True)
    recruiter_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    response_id = Column(Integer, ForeignKey('responses.id'), nullable=False)
    date = Column(DATE, nullable=False)
    time = Column(TIMESTAMP, nullable=False)
    
    users = relationship("User", back_populates="users")
    requests = relationship("Response", back_populates="responses")
    
    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "recruiter_id": self.recruiter_id,
            "response_id": self.response_id,
            "date": self.date,
            "time": self.time
        }