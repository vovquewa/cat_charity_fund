from typing import Optional

from pydantic import BaseSettings, EmailStr

from app.core.constants import (
    APP_TITLE,
    APP_DESCRIPTION,
    APP_VERSION,
)


class Settings(BaseSettings):
    app_title: str = APP_TITLE
    app_description: str = APP_DESCRIPTION
    app_version: str = APP_VERSION
    database_url: str = None
    secret: str = None
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = ".env"


settings = Settings()
