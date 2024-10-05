from .cruds.director import DirectorCRUD
from .cruds.recruiter import RecruiterCRUD
from .cruds.users import UsersCRUD
from .db import DatabaseManager


class CRUD(UsersCRUD, RecruiterCRUD, DirectorCRUD):
    def __init__(self, db_manager: DatabaseManager) -> None:
        self.db_manager = db_manager
