import traceback

from loguru import logger
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse

from src.database.crud import CRUD
from src.database.models import Role
from src.utils.oauth2_utils import OAuth2Utils


# TODO: Изменить логику аутентификации. Сделать через refresh токен.
class AdminAuth(AuthenticationBackend):
    def __init__(self, secret_key: str, db: CRUD, oauth2: OAuth2Utils) -> None:
        super().__init__(secret_key)
        self.db = db
        self.oauth2 = oauth2

    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form["username"], form["password"]

        user = await self.oauth2.validate_user(username, password)

        if user and user.role == Role.admin:
            access_token = await self.oauth2.create_access_token(
                {"username": str(user.username)}
            )
            request.session.update({"token": access_token})
            return True

        return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        if not token:
            return RedirectResponse(request.url_for("admin:login"), status_code=302)

        try:
            check_auth = self.oauth2.check_auth_token(token)
            if "username" in check_auth:
                user = await self.db.get_user_by_username(check_auth["username"])
                if user.role == Role.admin:
                    return True

            return RedirectResponse(request.url_for("admin:login"), status_code=302)
        except Exception:
            return RedirectResponse(request.url_for("admin:login"), status_code=302)
