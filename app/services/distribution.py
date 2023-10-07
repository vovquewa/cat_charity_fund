from datetime import datetime


def distribution(
    target,
    sources: list,
) -> list:
    changed_sources = []
    for source in sources:
        amount_to_invest = min(
            source.full_amount - source.invested_amount,
            target.full_amount - target.invested_amount
        )
        source.invested_amount += amount_to_invest
        target.invested_amount += amount_to_invest
        for item in target, source:
            if item.invested_amount == item.full_amount:
                item.fully_invested = True
                item.close_date = datetime.now()
                changed_sources.append(source)
        if target.fully_invested:
            break
    return changed_sources
