import json
from aiofiles import os
from fastapi import Request
from fastapi.responses import JSONResponse, FileResponse

from utils.json_custom_encoder import JSONCustomEncoder
from .routers import protected
import config as cfg
from database.models import Role


@protected.post("/get_my_account_info")
async def get_my_account_info(request: Request):
    user = request.state.user.to_dict()
    del user["hashed_password"]
    del user["refresh_token"]
    return JSONResponse(json.dumps(user, cls=JSONCustomEncoder))


@protected.get("/my_avatar")
async def get_my_avatar(request: Request):
    user = request.state.user.to_dict()
    image_path = cfg.USERS_AVATARS / "{username}.png".format(username=user["username"])
    

    if not await os.path.exists(image_path):
        if user["role"] == Role.director:
            image_path = cfg.DEFAULT_DIRECTOR_AVATAR
        elif user["role"] == Role.recruiter:
            image_path = cfg.DEFAULT_RECRUITER_AVATAR
        else:
            return JSONResponse(status_code=404, content={"message": "Image not found"})

    return FileResponse(image_path, media_type="image/png")
