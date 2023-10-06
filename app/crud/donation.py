from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.crud.base import CRUDBase
from app.models import Donation, User


class CRUDDonation(CRUDBase):
    async def get_by_user(
            self,
            user: User,
            session: AsyncSession,
    ):
        reservations = await session.execute(
            select(Donation).where(
                Donation.user_id == user.id
            )
        )
        return reservations.scalars().all()

    async def get_by_fully_invested(
        self,
        session: AsyncSession,
    ) -> list[Donation]:
        charityprojects = await session.execute(
            select(Donation).where(
                Donation.fully_invested == False
            )
        )
        return charityprojects.scalars().all()


donation_crud = CRUDDonation(Donation)
