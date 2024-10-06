from contextlib import asynccontextmanager

from fastapi import FastAPI
from loguru import logger
from sqladmin import Admin
from starlette.middleware.cors import CORSMiddleware

import config as cfg
from database.crud import CRUD
from database.db import DatabaseManager
from database.sqladmin_views import all_views
from utils.oauth2_utils import OAuth2Utils
from utils.sqladmin_auth import AdminAuth



@asynccontextmanager
async def lifespan(_):
    yield
    logger.info("Завершение работы сервера!")

app: FastAPI = FastAPI(lifespan=lifespan, debug=True)

db_manager = DatabaseManager(cfg.DB_URL)
db = CRUD(db_manager)
oauth2: OAuth2Utils = OAuth2Utils(
    db=db,
    jwt_token_secret=cfg.JWT_TOKEN_SECRET,
    access_token_exp=cfg.JWT_ACCESS_TOKEN_EXPIRE_MINUTES,
    refresh_token_exp=cfg.JWT_REFRESH_TOKEN_EXPIRE_MINUTES,
    jwt_algorithm=cfg.JWT_ALGORITHM,
    token_url="/api/auth/login",
)

##==> Admin panel
#########################################
admin = Admin(
    app,
    db_manager.engine,
    authentication_backend=AdminAuth(cfg.JWT_TOKEN_SECRET, db, oauth2),
)
for view in all_views:
    admin.add_view(view)
#########################################

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
