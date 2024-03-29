from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.donation import donation_crud
from app.crud.charityproject import charityproject_crud
from app.models.user import User
from app.schemas.donation import (DonationCreate, DonationDB,
                                  DonationDBPostGetMy)
from app.services.distribution import distribution

router = APIRouter()


@router.get(
    '/',
    description='Только для суперюзеров.\n\nВозвращает список всех пожертвований.',
    dependencies=[Depends(current_superuser)],
    response_model=list[DonationDB],
    response_model_exclude_none=True,
)
async def get_all_donations(
        session: AsyncSession = Depends(get_async_session),
):
    return await donation_crud.get_multi(session)


@router.post(
    '/',
    description='Сделать пожертвование.',
    response_model=DonationDBPostGetMy,
    response_model_exclude_none=True,
)
async def create_donation(
        donation: DonationCreate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
):
    donation = await donation_crud.create(
        donation,
        session,
        user,
        commit=False
    )
    donation.invested_amount = 0
    changed = distribution(
        donation,
        await charityproject_crud.get_by_fully_invested(
            session=session
        )
    )
    session.add_all(changed)
    await session.commit()
    await session.refresh(donation)
    return donation


@router.get(
    '/my',
    description='Вернуть список пожертвований пользователя, выполняющего запрос.',
    response_model=list[DonationDBPostGetMy],
    response_model_exclude_none=True,
)
async def get_user_donations(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    return await donation_crud.get_by_user(user, session)
