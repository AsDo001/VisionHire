import asyncio
import random
from datetime import datetime, timedelta
from faker import Faker

import sys
import os
from pathlib import Path

print(Path(__file__).parent.parent)

module_path = os.path.abspath(str(Path(__file__).parent.parent))
sys.path.append(module_path)

from src.database.models import User, Role, Vacancy, Candidate, CandidateStatus, Task, Interview
from src.loader import oauth2, db_manager
from sqlalchemy.future import select

fake = Faker()


async def create_fake_users(num_users):
    roles = list(Role)
    users = []
    for _ in range(num_users):
        users.append(User(
            username=fake.user_name(),
            name=fake.name(),
            email=fake.email(),
            role=random.choice(roles),
            hashed_password=random.choice([oauth2.get_password_hash(i) for i in ["1234", "1111", "2222", "12345"]]),
            refresh_token=None,
            created_at=datetime.now()
        ))

    async with db_manager.get_session() as session:
        session.add_all(users)
        await session.commit()


async def create_fake_vacancies(num_vacancies):
    async with db_manager.get_session() as session:
        result = await session.execute(select(User))
        users = result.scalars().all()

        for _ in range(num_vacancies):
            vacancy = Vacancy(
                title=fake.job(),
                description=fake.text(max_nb_chars=200),
                location=fake.city(),
                creator_username=random.choice(users).username,
                created_at=datetime.now(),
                status=random.choice([True, False])
            )
            session.add(vacancy)
        await session.commit()


async def create_fake_candidates(num_candidates):
    async with db_manager.get_session() as session:
        result = await session.execute(select(Vacancy))
        vacancies = result.scalars().all()

        for _ in range(num_candidates):
            candidate = Candidate(
                first_name=fake.first_name(),
                family_name=fake.last_name(),
                surname=fake.last_name(),
                phone=fake.phone_number(),
                email=fake.email(),
                city=fake.city(),
                vacancy_id=random.choice(vacancies).id,
                resume_file=fake.file_path(extension='pdf'),
                created_at=datetime.now(),
                updated_at=datetime.now(),
                recruiter_description=fake.text(max_nb_chars=100),
                status=random.choice(list(CandidateStatus))
            )
            session.add(candidate)

        await session.commit()


async def create_fake_tasks(num_tasks):
    async with db_manager.get_session() as session:
        result = await session.execute(select(User))
        users = result.scalars().all()

        for _ in range(num_tasks):
            task = Task(
                title=fake.sentence(nb_words=6),
                description=fake.text(max_nb_chars=200),
                status=random.choice([True, False]),
                task_creator=random.choice(users).username,
                task_receiver=random.choice(users).username,
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
            session.add(task)
        await session.commit()


async def create_fake_interviews(num_interviews):
    async with db_manager.get_session() as session:
        result_users = await session.execute(select(User))
        users = result_users.scalars().all()

        result_candidates = await session.execute(select(Candidate))
        candidates = result_candidates.scalars().all()

        for _ in range(num_interviews):
            interview = Interview(
                recruiter_username=random.choice(users).username,
                candidate_id=random.choice(candidates).id,
                datetime=datetime.now() + timedelta(days=random.randint(1, 30))
            )
            session.add(interview)
        await session.commit()


async def main():
    await create_fake_users(30)
    await create_fake_vacancies(10)
    await create_fake_candidates(40)
    await create_fake_tasks(13)
    await create_fake_interviews(3)


if __name__ == "__main__":
    asyncio.run(main())
