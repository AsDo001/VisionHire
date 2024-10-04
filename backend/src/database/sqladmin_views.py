from sqladmin import ModelView

from .models import User


class UsersView(ModelView, model=User):
    column_list = [
        User.username,
        User.name,
        User.email,
        User.role,
        User.hashed_password,
        User.refresh_token,
        User.created_at,
    ]


all_views = [UsersView]
