from sqlalchemy import Column, String, Text

from app.models.investment import InvestmentModel


class CharityProject(InvestmentModel):
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text, nullable=False)
