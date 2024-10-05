from pydantic import BaseModel
from datetime import datetime


class CreateVacancies(BaseModel):
    title:str
    description:str
    location:str
    recruiter_username:int
    created_at:datetime
    user_username:int


class CreateInterview(BaseModel):
    
    recruiter_username:int
    date_time:datetime
    user_username:int