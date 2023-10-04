from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models import CharityProject, Donation


async def distribution(
        session: AsyncSession,
):
    charityprojects = await session.execute(
        select(CharityProject).where(
            CharityProject.fully_invested == bool(False)
        )
    )
    charityprojects = charityprojects.scalars().all()
    if charityprojects:
        for charityproject in charityprojects:
            donations = await session.execute(
                select(Donation).where(
                    Donation.fully_invested == bool(False)
                )
            )
            donations = donations.scalars().all()
            if donations:
                for donation in donations:
                    donation_remains = donation.full_amount - donation.invested_amount
                    charityproject_remains = charityproject.full_amount - charityproject.invested_amount
                    if donation_remains >= charityproject_remains:
                        donation.invested_amount += charityproject_remains
                        charityproject.invested_amount += charityproject_remains
                        charityproject.fully_invested = bool(True)
                        charityproject.close_date = datetime.now()
                        if donation.invested_amount == donation.full_amount:
                            donation.fully_invested = bool(True)
                            donation.close_date = datetime.now()
                        if charityproject.invested_amount == charityproject.full_amount:
                            charityproject.fully_invested = bool(True)
                            charityproject.close_date = datetime.now()
                        if charityproject.fully_invested:
                            break
                    donation.invested_amount += donation_remains
                    charityproject.invested_amount += donation_remains
                    if donation.invested_amount == donation.full_amount:
                        donation.fully_invested = bool(True)
                        donation.close_date = datetime.now()
            else:
                break
    await session.commit()

    return charityprojects
