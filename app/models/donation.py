from sqlalchemy import Column, ForeignKey, Integer, Text

from app.models.investment import InvestmentModel


class Donation(InvestmentModel):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text, nullable=True)
