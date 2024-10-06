from loguru import logger
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse

from src.database.crud import CRUD
from src.database.models import Role
from src.utils.oauth2_utils import OAuth2Utils
import src.config as cfg


# TODO: Изменить логику аутентификации. Сделать через refresh токен.
class AdminAuth(AuthenticationBackend):
    def __init__(self, secret_key: str, db: CRUD, oauth2: OAuth2Utils) -> None:
        super().__init__(secret_key)
        self.db = db
        self.oauth2 = oauth2

    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form["username"], form["password"]

        if username != cfg.ADMIN_LOGIN or password != cfg.ADMIN_PASSWORD:
            logger.error(f"Invalid admin credentials: {username}:{password}")
            return False

        access_token = await self.oauth2.create_access_token({"username": username})
        request.session.update({"token": access_token})
        logger.info(f"Admin logged in: {username}")
        return True

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        if not token:
            return RedirectResponse(request.url_for("admin:login"), status_code=302)

        try:
            check_auth = self.oauth2.check_auth_token(token)
            logger.info(f"Admin authenticated: {check_auth}")
            if "username" in check_auth:
                if check_auth["username"] == cfg.ADMIN_LOGIN:
                    return True

            return RedirectResponse(request.url_for("admin:login"), status_code=302)
        except Exception:
            return RedirectResponse(request.url_for("admin:login"), status_code=302)
