from http import HTTPStatus

from fastapi import APIRouter, HTTPException

from app.core.user import auth_backend, fastapi_users
from app.schemas.user import UserCreate, UserRead, UserUpdate

DO_NOT_DELETE = "Не используйте удаление, деактивируйте пользователей."
DELETE_NOT_ALLOWED = "Удаление пользователей запрещено!"

router = APIRouter()


@router.delete(
    '/users/{id}',
    tags=['users'],
    deprecated=True,
)
def delete_user(id: str):
    raise HTTPException(
        status_code=HTTPStatus.METHOD_NOT_ALLOWED,
        detail=DELETE_NOT_ALLOWED
    )


router.include_router(

    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth/jwt',
    tags=['auth'],
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['auth'],
)


router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix='/users',
    tags=['users'],
)


@router.delete(
    '/users/{id}',
    tags=['users'],
    deprecated=True,
    description=DO_NOT_DELETE
)
def delete_user(id: str):
    pass