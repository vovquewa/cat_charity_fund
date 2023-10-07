from datetime import datetime

from app.models import InvestmentModel


def distribution(
    target: InvestmentModel,
    sources: list[InvestmentModel],
) -> list[InvestmentModel]:
    changed_sources = []
    for source in sources:
        amount_to_invest = min(
            source.full_amount - source.invested_amount,
            target.full_amount - target.invested_amount
        )
        changed_sources.append(source)
        for item in target, source:
            item.invested_amount += amount_to_invest
            if item.invested_amount == item.full_amount:
                item.fully_invested = True
                item.close_date = datetime.now()
        if target.fully_invested:
            break
    return changed_sources
