from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (
    check_charityproject_exists,
    check_charityproject_full_amount,
    check_charityproject_is_closed,
    check_charityproject_is_fully_invested,
    check_charityproject_is_in_progress,
    check_charityproject_name_duplicate
)
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud.charityproject import charityproject_crud
from app.schemas.charityproject import (
    CharityProjectCreate,
    CharityProjectCreateDB,
    CharityProjectDB,
    CharityProjectUpdate
)
from app.services.distribution import distribution

router = APIRouter()


@router.post(
    '/',
    description='Только для суперюзеров.\n\nСоздаёт благотворительный проект.',
    response_model=CharityProjectCreateDB,
    dependencies=[Depends(current_superuser)],
    response_model_exclude_none=True,
)
async def create_charity_project(
        charityproject: CharityProjectCreate,
        session: AsyncSession = Depends(get_async_session),
):
    await check_charityproject_name_duplicate(charityproject.name, session)
    new_charityproject = await charityproject_crud.create(charityproject, session)
    await distribution(session)
    await session.refresh(new_charityproject)
    return new_charityproject


@router.get(
    '/',
    description='Возвращает список всех проектов.',
    response_model=list[CharityProjectCreateDB],
    response_model_exclude={'close_date'},
)
async def get_all_charity_projects(
        session: AsyncSession = Depends(get_async_session),
):
    all_reservations = await charityproject_crud.get_multi(session)
    return all_reservations


@router.delete(
    '/{project_id}',
    description='Только для суперюзеров.\n\nУдаляет проект. Нельзя удалить проект, в который уже были инвестированы средства, его можно только закрыть.',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
)
async def delete_charity_project(
    project_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    charityproject = await check_charityproject_exists(project_id, session)
    await check_charityproject_is_closed(project_id, session)
    await check_charityproject_is_in_progress(project_id, session)
    charityproject = await charityproject_crud.remove(charityproject, session)
    return charityproject


@router.patch(
    '/{project_id}',
    description='Только для суперюзеров.\n\nЗакрытый проект нельзя редактировать; нельзя установить требуемую сумму меньше уже вложенной.',
    response_model=CharityProjectDB,
    # response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def update_charity_project(
        project_id: int,
        charityproject_in: CharityProjectUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    charityproject = await check_charityproject_exists(project_id, session)
    if charityproject_in.name:
        await check_charityproject_name_duplicate(charityproject_in.name, session)
    charityproject = await charityproject_crud.update(charityproject, charityproject_in, session)
    await check_charityproject_full_amount(project_id, session)
    await check_charityproject_is_fully_invested(project_id, session)
    return charityproject


@router.get(
    '/test',
)
async def get_invested(
        session: AsyncSession = Depends(get_async_session),
):
    distributions = await distribution(session)
    print(distributions)
    return distributions