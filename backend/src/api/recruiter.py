from fastapi import HTTPException, Request
from fastapi.responses import Response
from src.loader import db

from ..database.models import User, Role
from ..schemas.recruiter import CreateInterview, CreateVacancies
from .routers import protected


@protected.post("/create_vacancies")
async def create_vacancies(request: Request, vacancies_data: CreateVacancies):
    user: User = request.state.user.to_dict()

    if user["role"] == Role.recruiter.value:
        await db.create_vacancy(
            title=vacancies_data.title,
            description=vacancies_data.description,
            location=vacancies_data.location,
            recruiter_username=vacancies_data.recruiter_username,
            created_at=vacancies_data.created_at
        )

    return HTTPException(status_code=403)


@protected.post("/create_interview")
async def create_contributes(request: Request, interview_data: CreateInterview):
    user: User = request.state.user.to_dict()

    if user["role"] != Role.recruiter.value:
        raise HTTPException(status_code=403, detail="Вы не рекрутер")
    
    await db.create_interview(
        recruiter_username=interview_data.recruiter_username,
        candidate_id=interview_data.candidate_id,
        interview_datetime=interview_data.datetime
    )

    return Response(status_code=200)
