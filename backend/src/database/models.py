import enum
from datetime import datetime
from typing import Any

from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import ENUM as PgEnum
from sqlalchemy.orm import relationship

from .db import Base


class Role(enum.Enum):
    recruiter = "recruiter"
    director = "director"


class CandidateStatus(enum.Enum):
    expected = "expected"
    appointed = "appointed"
    accepted = "accepted"
    rejected = "rejected"


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
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now)

    vacancies = relationship("Vacancy", back_populates="recruiter")
    tasks_creator = relationship(
        "Task", back_populates="creator", foreign_keys="Task.task_creator"
    )
    tasks_receiver = relationship(
        "Task", back_populates="receiver", foreign_keys="Task.task_receiver"
    )
    interviews = relationship("Interview", back_populates="recruiter")

    subordinate_roles = relationship("Hierarchy", foreign_keys="[Hierarchy.sub_id]", back_populates="subordinate")
    supervisor_roles = relationship("Hierarchy", foreign_keys="[Hierarchy.super_id]", back_populates="supervisor")

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


class Hierarchy(Base):
    __tablename__ = "hierarchies"
    id = Column(Integer, primary_key=True, autoincrement=True)
    sub_id = Column(String, ForeignKey('users.username'), nullable=False)
    super_id = Column(String, ForeignKey('users.username'), nullable=False)

    subordinate = relationship("User", foreign_keys=[sub_id], back_populates="supervisor_roles")
    supervisor = relationship("User", foreign_keys=[super_id], back_populates="subordinate_roles")

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "sub_id": self.sub_id,
            "super_id": self.super_id,
        }


class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    family_name = Column(String, nullable=False)
    surname = Column(String, nullable=True)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    city = Column(String, nullable=False)
    vacancy_id = Column(Integer, ForeignKey("vacancies.id"), nullable=False)
    resume_file = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now)
    updated_at = Column(TIMESTAMP, nullable=False, default=datetime.now)
    recruiter_description = Column(String, nullable=True)
    status = Column(
        PgEnum(CandidateStatus, name="candidate_status", create_type=False),
        nullable=False,
        default=CandidateStatus.expected,
    )

    vacancy = relationship("Vacancy", back_populates="candidates")
    interviews = relationship("Interview", back_populates="candidate")

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
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "recruiter_description": self.recruiter_description,
            "status": self.status,
        }


class Vacancy(Base):
    __tablename__ = "vacancies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    location = Column(String, nullable=False)
    creator_username = Column(String, ForeignKey("users.username"), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now)
    status = Column(Boolean, nullable=False)

    recruiter = relationship("User", back_populates="vacancies")
    candidates = relationship("Candidate", back_populates="vacancy")

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "location": self.location,
            "creator_username": self.creator_username,
            "created_at": self.created_at,
            "status": self.status,
        }


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status = Column(Boolean, nullable=False, default=False)
    task_creator = Column(String, ForeignKey("users.username"), nullable=False)
    task_receiver = Column(String, ForeignKey("users.username"), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now)
    updated_at = Column(TIMESTAMP, nullable=False, default=datetime.now)

    creator = relationship(
        "User", back_populates="tasks_creator", foreign_keys=[task_creator]
    )
    receiver = relationship(
        "User", back_populates="tasks_receiver", foreign_keys=[task_receiver]
    )

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "task_creator": self.task_creator,
            "task_receiver": self.task_receiver,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }


class Interview(Base):
    __tablename__ = "interviews"
    id = Column(Integer, primary_key=True, autoincrement=True)
    recruiter_username = Column(String, ForeignKey("users.username"), nullable=False)
    candidate_id = Column(Integer, ForeignKey("candidates.id"), nullable=False)
    datetime = Column(TIMESTAMP, nullable=False)

    recruiter = relationship("User", back_populates="interviews")
    candidate = relationship("Candidate", back_populates="interviews")

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "recruiter_username": self.recruiter_username,
            "candidate_id": self.candidate_id,
            "datetime": self.datetime,
        }
