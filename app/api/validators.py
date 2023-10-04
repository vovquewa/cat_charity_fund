from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charityproject import charityproject_crud
from app.models import CharityProject


async def check_charityproject_name_duplicate(
        charityproject_name: str,
        session: AsyncSession,
) -> None:
    room_id = await charityproject_crud.get_id_by_name(charityproject_name, session)
    if room_id is not None:
        raise HTTPException(
            status_code=400,
            detail='Проект с таким именем уже существует!',
        )


async def check_charityproject_exists(
        charityproject_id: int,
        session: AsyncSession,
) -> CharityProject:
    charityproject = await charityproject_crud.get(charityproject_id, session)
    if charityproject is None:
        raise HTTPException(
            status_code=404,
            detail='Проект не найден!'
        )
    return charityproject


async def check_charityproject_is_closed(
        charityproject_id: int,
        session: AsyncSession,
):
    charityproject = await check_charityproject_exists(charityproject_id, session)
    if charityproject.fully_invested == bool(True):
        raise HTTPException(
            status_code=400,
            detail='В проект были внесены средства, не подлежит удалению!'
        )


async def check_charityproject_is_fully_invested(
        charityproject_id: int,
        session: AsyncSession,
):
    charityproject = await check_charityproject_exists(charityproject_id, session)
    if charityproject.fully_invested == bool(True):
        raise HTTPException(
            status_code=400,
            detail='Закрытый проект нельзя редактировать!'
        )


async def check_charityproject_is_in_progress(
        charityproject_id: int,
        session: AsyncSession,
):
    chariryproject = await check_charityproject_exists(charityproject_id, session)
    if chariryproject.fully_invested == bool(False) and chariryproject.invested_amount > 0:
        raise HTTPException(
            status_code=400,
            detail='В проект были внесены средства, не подлежит удалению!'
        )


async def check_charityproject_full_amount(
        charityproject_id: int,
        session: AsyncSession,
):
    chariryproject = await check_charityproject_exists(charityproject_id, session)
    if chariryproject.invested_amount > chariryproject.full_amount:
        raise HTTPException(
            status_code=400,
            detail='Нельзя установить требуемую сумму меньше уже вложенной!'
        )