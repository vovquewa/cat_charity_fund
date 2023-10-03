from fastapi import FastAPI

from app.core.config import settings
from app.api.routers import main_router
from app.core.init_db import create_first_superuser

app = FastAPI(
    title=settings.app_title,
    description=settings.app_description,
    version=settings.app_version,
)


app.include_router(main_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.on_event('startup')
async def startup():
    await create_first_superuser()