from datetime import datetime
from typing import List

from sqlalchemy.future import select
from sqlalchemy import extract, func
from collections import defaultdict

from ..db import DatabaseManager
from ..models import Candidate, Interview, Task, Vacancy, CandidateStatus, Hierarchy


class RecruiterCRUD:
    db_manager: DatabaseManager

    async def create_vacancy(
        self,
        title: str,
        description: str,
        location: str,
        recruiter_username: str,
        created_at: str,
    ) -> Vacancy:
        async with self.db_manager.get_session() as session:
            new_vacancies = Vacancy(
                title=title,
                description=description,
                location=location,
                recruiter_username=recruiter_username,
                created_at=created_at,
            )

            session.add(new_vacancies)
            await session.commit()
            await session.refresh(new_vacancies)
            return new_vacancies

    async def get_vacancies(self, recruiter_username: str) -> List[Vacancy]:
        '''все вакансии созданные рекрутером'''
        async with self.db_manager.get_session() as session:
            result = await session.execute(
                select(Vacancy).where(Vacancy.creator_username == recruiter_username)
            )
            vacancies = result.scalars().all()
            return vacancies

    async def get_subs_vacancies(self, user_id: str) -> List[Vacancy]:
        '''все вакансии созданные подчиненными'''
        subs = await self.get_subs(user_id)
        async with self.db_manager.get_session() as session:

            result = await session.execute(
                select(Vacancy).where(Vacancy.creator_username == 1)
            )
            vacancies = result.scalars().all()
            return vacancies
        
    async def create_interview(
        self, recruiter_username: str, candidate_id: int, interview_datetime: datetime
    ) -> Interview:
        async with self.db_manager.get_session() as session:
            new_interview = Interview(
                recruiter_username=recruiter_username,
                candidate_id=candidate_id,
                datetime=interview_datetime,
            )

            session.add(new_interview)
            await session.commit()
            await session.refresh(new_interview)
            return new_interview

    async def get_candidates(self, vacancy_id: int) -> List[Candidate]:
        '''все кандидаты по конкретной вакансии'''
        async with self.db_manager.get_session() as session:
            result = await session.execute(
                select(Candidate).where(Candidate.vacancy_id == vacancy_id)
            )
            candidates = result.scalars().all()
            return candidates

    async def get_tasks(self, username: str) -> List[Task]:
        '''все задачи конкретного пользователя'''
        async with self.db_manager.get_session() as session:
            usr_tasks: List[Task] = await session.execute(
                select(Task).where(Task.task_receiver == username)
            )
            return usr_tasks.scalars().all()

    async def create_task(self, title: str, description: str, id_creator: int, id_receiver: int) -> List[Task]:
        async with self.db_manager.get_session() as session:
            await session.add(
                Task(title=title, description=description, task_creator=id_creator, task_receiver=id_receiver)
            )
    
    async def update_task(self, id_task: int) -> List[Task]:
        async with self.db_manager.get_session() as session:
            update_record = await session.query(Task).filter(Task.id == id_task).first()
            update_record.status = not update_record.status
            await session.commit()

    async def get_new_candidates(self, username: str) -> int:
        '''число всех новых кандидатов для метрики'''
        async with self.db_manager.get_session() as session:
            result = await session.execute(
                select(func.count()).where(Candidate.status == CandidateStatus.expected)
            )
            return result.scalar()
        

    async def get_new_condidates_bymonth(self, username: str) -> List[Task]:
        '''новые кандидаты по месяцам для метрики'''
        async with self.db_manager.get_session() as session:
            results = (
                await session.query(
                    extract('year', Candidate.created_at).label('year'),
                    extract('month', Candidate.created_at).label('month'),
                    func.count(Candidate.id).label('count')
                )
                .group_by('year', 'month')
                .order_by('year', 'month')
                .all()
            )

            data = defaultdict(lambda: defaultdict(int))
            months_map = {
                1: "Январь",
                2: "Февраль",
                3: "Март",
                4: "Апрель",
                5: "Май",
                6: "Июнь",
                7: "Июль",
                8: "Август",
                9: "Сентябрь",
                10: "Октябрь",
                11: "Ноябрь",
                12: "Декабрь"
            }

            for year, month, count in results:
                month_name = months_map[month]
                data[year][month_name] = count

            return data
    async def get_accepted_condidates_bymonth(self, username: str) -> List[Task]:
        '''принятые кандидаты по месяцам для метрики'''
        async with self.db_manager.get_session() as session:
            results = (
                await session.query(
                    extract('year', Candidate.updated_at).label('year'),
                    extract('month', Candidate.updated_at).label('month'),
                    func.count(Candidate.id).label('count')
                )
                .group_by('year', 'month')
                .order_by('year', 'month')
                .all()
            )

            data = defaultdict(lambda: defaultdict(int))
            months_map = {
                1: "Январь",
                2: "Февраль",
                3: "Март",
                4: "Апрель",
                5: "Май",
                6: "Июнь",
                7: "Июль",
                8: "Август",
                9: "Сентябрь",
                10: "Октябрь",
                11: "Ноябрь",
                12: "Декабрь"
            }

            for year, month, count in results:
                month_name = months_map[month]
                data[year][month_name] = count

            return data

    async def get_subs(self, user_id: int) -> List[int]:
        '''список id подчиненных для назначения задач'''
        async with self.db_manager.get_session() as session:
            result = await session.execute(
                select(Hierarchy.sub_id).where(Hierarchy.super_id == user_id)
            )
            subs = result.scalars().all()
            return subs
        


    
    