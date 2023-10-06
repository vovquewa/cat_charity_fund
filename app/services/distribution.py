from datetime import datetime
from typing import Union

from app.models import Donation, CharityProject


def distribution(
    target: Union[CharityProject, Donation],
    sources: list[Union[CharityProject, Donation]],
):
    for source in sources:
        source_remains = source.full_amount - source.invested_amount
        target_remains = target.full_amount - target.invested_amount
        amount_to_invest = min(source_remains, target_remains)
        source.invested_amount += amount_to_invest
        target.invested_amount += amount_to_invest
        if source.invested_amount == source.full_amount:
            source.fully_invested = bool(True)
            source.close_date = datetime.now()
        if target.invested_amount == target.full_amount:
            target.fully_invested = bool(True)
            target.close_date = datetime.now()
        if target.fully_invested:
            break

    return sources
