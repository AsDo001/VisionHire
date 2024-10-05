# from ..db import DatabaseManager

# from ..models import Vacancies, Interview, User
# from datetime import datetime


# class DirectorCRUD:
#     db_manager: DatabaseManager


#     async def add_recruiter(
#             self,
#             username:str, 
#             name:str, 
#             email:str,
#             role:str,
#             hashed_password:str,
#             refresh_token:str,
#             created_at:datetime,
#             ):
        
#         async with self.db_manager.get_session() as session:
#             new_recruiter = User(
#                 username=username,
#                 name=name,
#                 email=email,
#                 role=role,
#                 hashed_password=hashed_password,
#                 refresh_token=refresh_token,
#                 created_at=created_at
#             )

#             session.add(new_recruiter)
#             await session.commit()
#             await session.refresh(new_recruiter)
#             return new_recruiter
