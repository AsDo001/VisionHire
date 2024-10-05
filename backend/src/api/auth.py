from email_validator import EmailNotValidError, validate_email
from fastapi import HTTPException, Request
from fastapi.responses import Response

from src.loader import db, oauth2
from src.schemas.auth import ChangePassword, Login, Register, UpdatedTokens

from ..database.models import User
from .errors import credentials_exc, login_data_exc, username_exits_exc
from .routers import protected, unprotected


@unprotected.post("/auth/register")
async def register(form: Register, response: Response):
    try:
        validated_email = validate_email(form.email)
        form.email = validated_email["email"]
    except EmailNotValidError:
        raise HTTPException(status_code=400, detail="Неверный email!")

    if len(form.username) < 1 or len(form.name) < 1:
        raise HTTPException(
            status_code=400,
            detail="Имя пользователя должно быть длиной не менее 1 символа!",
        )

    if len(form.password) < 4:
        raise HTTPException(
            status_code=400, detail="Пароль должен быть длиной не менее 4 символов!"
        )

    db_user = await db.get_user_by_username(username=form.username)

    if db_user:
        raise username_exits_exc

    await db.create_user(
        form.username, form.name, form.email, oauth2.get_password_hash(form.password)
    )
    tokens: UpdatedTokens = await oauth2.update_access_and_refresh_tokens(form.username)
    response.set_cookie(key="access_token", value=tokens.access_token, httponly=True)
    response.set_cookie(key="refresh_token", value=tokens.refresh_token, httponly=True)
    response.status_code = 200
    return response


@unprotected.post("/auth/login")
async def login(form: Login, response: Response):
    user = await oauth2.validate_user(form.username, form.password)

    if not user:
        raise login_data_exc

    tokens = await oauth2.update_access_and_refresh_tokens(form.username)
    response.set_cookie(key="access_token", value=tokens.access_token, httponly=True)
    response.set_cookie(key="refresh_token", value=tokens.refresh_token, httponly=True)
    response.status_code = 200
    return response


@unprotected.post("/auth/is_authenticated")
async def is_authenticated(request: Request, response: Response):
    access_token = request.cookies.get("access_token", None)
    refresh_token = request.cookies.get("refresh_token", None)
    is_authenticated = await oauth2.check_and_update_auth(access_token, refresh_token)

    if is_authenticated.is_authenticated:
        response.status_code = 200
        response.set_cookie(
            key="access_token", value=is_authenticated.access_token, httponly=True
        )
        response.set_cookie(
            key="refresh_token", value=is_authenticated.refresh_token, httponly=True
        )
        return response
    else:
        raise credentials_exc


@protected.post("/auth/change_password")
async def change_password(request: Request, form: ChangePassword):
    user: User = request.state.user

    if not oauth2.verify_password(form.old_password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Старый пароль неверен!")

    if len(form.new_password) < 4:
        raise HTTPException(
            status_code=400,
            detail="Новый пароль должен быть длиной не менее 4 символов!",
        )

    if form.new_password != form.confirm_password:
        raise HTTPException(status_code=400, detail="Пароли не совпадают!")

    await db.update_password_by_username(
        user.username, oauth2.get_password_hash(form.new_password)
    )
    return Response(status_code=200)


@unprotected.post("/auth/logout")
async def logout(request: Request, response: Response):
    response.delete_cookie(key="access_token", httponly=True)
    response.delete_cookie(key="refresh_token", httponly=True)
    response.status_code = 200
    return response
