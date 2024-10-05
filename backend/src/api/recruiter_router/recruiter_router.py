from ..routers import protected
from fastapi import Request
from ...database.models import User

from fastapi import HTTPException
from .schemas import CreateVacancies, CreateInterview
from src.loader import db


@protected.post("/create_vacancies")
async def create_vacancies(request:Request, vacancies_data:CreateVacancies):
    user: User = request.state.user.to_dict()

    if user["role"] == "recruiter":

        await db.create_vacancies(
            vacancies_data.title, 
            vacancies_data.description,
            vacancies_data.location,
            vacancies_data.recruiter_username,
            vacancies_data.created_at,
            vacancies_data.user_username
            )

    return HTTPException(status_code=403)
  

#добавить рассылку на почту

@protected.post("/create_interview")
async def create_contributes(request:Request,interview_data:CreateInterview):
    user:User = request.state.user.to_dict()
    
    if user["role"] == "recruiter":
        user = await db.get_user_by_username(interview_data.user_username)
        if user:
        
            await db.create_interview(
                interview_data.recruiter_username,
                interview_data.date_time,
                interview_data.user_username
            )

        return "такого пользователя нет"
    return HTTPException(status_code=403)
