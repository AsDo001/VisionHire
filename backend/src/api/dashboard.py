from fastapi import HTTPException, Request
from loader import db
from typing import List, Dict

from database.models import User, Vacancy, Candidate, Role
from .routers import protected
from schemas.recruiter import CreateTask


@protected.post('/get_candidates')
async def get_candidates(request: Request):
    user: User = request.state.user.to_dict()

    if user["role"] == Role.recruiter.value:
        vacancies: List[Vacancy] = await db.get_vacancies(recruiter_username=user["username"])
        results: Dict[int, List[Candidate]] = {}

        for v in vacancies:
            candidates = await db.get_candidates(vacancy_id=v.id)
            results.update({v.id: candidates})

        return results
    
    return HTTPException(status_code=403, detail="Вы не рекрутер")


@protected.post('/get_tasks')
async def get_tasks(request: Request):
    user: User = request.state.user.to_dict()

    if user["role"] in [Role.recruiter.value, Role.director.value]:
        tasks = await db.get_tasks(user["username"])
        return tasks
    else:
        return HTTPException(status_code=403, detail="Ваша роль не позволяет просматривать задания")


@protected.post("/create_tasks")
async def create_tasks(request: Request, task_data:CreateTask):
    user: User = request.state.user.to_dict()
    task_creator = user["username"]

    if user["role"] == Role.recruiter.value:
        await db.create_task(title=task_data.title, description=task_data.description, id_creator=task_creator, id_receiver=task_creator)

    elif user["role"] == Role.director.value:
            await db.create_task(title=task_data.title, description=task_data.description, id_creator=task_creator, id_receiver=task_data.task_receiver)
    else:
        return HTTPException(status_code=403, detail="Ваша роль не позволяет просматривать задания")


@protected.post("/update_task")
async def update_task(request: Request, task_id: int):
    user: User = request.state.user.to_dict()

    if user["role"] in [Role.recruiter.value, Role.director.value]:
        await db.update_task(task_id=task_id, status=True)
    else:
        return HTTPException(status_code=403, detail="Ваша роль не позволяет изменять статус задания")

@protected.post("/get_data_for_graphs")
async def get_data_for_graphs(request: Request):
    user: User = request.state.user.to_dict()