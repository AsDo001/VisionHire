# from ..routers import protected
# from fastapi import Request
# from .schemas import CreateRecruiter
# from ...database.models import User
# from fastapi import HTTPException
# from src.loader import oauth2
# from src.loader import db
# from datetime import datetime


# @protected.get("/get_recruiter_interview_and_tasks")
# async def get_recruiter_interview_and_tasks(request:Request):
#     user:User = request.state.user.to_dict()



# @protected.post("/create_recruiter")
# async def create_recruiter(request:Request,recruiter_data:CreateRecruiter):
#     user:User = request.state.user.to_dict()

#     if user["role"] == "director":
#         hashed_password = oauth2.get_password_hash(recruiter_data.password)
#         role = "recruiter"
#         refresh_token = oauth2.create_refresh_token(recruiter_data.username)
#         # director_username = user["username"]
#         created_at = datetime.now()

#         await db.add_recruiter(
#             recruiter_data.username, 
#             recruiter_data.name,
#             recruiter_data.email,
#             role,
#             hashed_password,
#             refresh_token,
#             created_at,
          
#             )
       

        
#     return HTTPException(status_code=403)


