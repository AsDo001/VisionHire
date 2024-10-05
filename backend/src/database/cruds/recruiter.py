from ..db import DatabaseManager

from ..models import Vacancy, Interview

class RecruiterCRUD:
    db_manager: DatabaseManager


    async def create_vacancies(self, title,description,location,recruiter_username,created_at, users_username):
        async with self.db_manager.get_session() as session:

            new_vacancies = Vacancy(
                title=title,
                description=description,
                location=location,
                recruiter_username=recruiter_username,
                created_at=created_at,
                users=users_username)
            
            session.add(new_vacancies)
            await session.commit()
            await session.refresh(new_vacancies)
            return new_vacancies
        
    async def create_interview(self,recruiter_username, date_time, users_username):
        async with self.db_manager.get_session() as session:

            new_interview = Interview(
                recruiter_username=recruiter_username,
                date_time=date_time,
                users=users_username
            )

            session.add(new_interview)
            await session.commit()
            await session.refresh(new_interview)
            return new_interview
        

    


