from datetime import datetime
from app.models import CharityProject, Donation


def distribution(
        charityprojects: list[CharityProject],
        donations: list[Donation]
):
    for charityproject in charityprojects:
        for donation in donations:
            donation_remains = donation.full_amount - donation.invested_amount
            charityproject_remains = (
                charityproject.full_amount - charityproject.invested_amount
            )
            amount_to_invest = min(donation_remains, charityproject_remains)
            donation.invested_amount += amount_to_invest
            charityproject.invested_amount += amount_to_invest
            if donation.invested_amount == donation.full_amount:
                donation.fully_invested = bool(True)
                donation.close_date = datetime.now()
            if charityproject.invested_amount == charityproject.full_amount:
                charityproject.fully_invested = bool(True)
                charityproject.close_date = datetime.now()
            if charityproject.fully_invested:
                break

    return charityprojects, donations
