from sqlalchemy import Boolean, Column, Integer, String, Text

from app.core.db import Base
from app.models.basetemplate import DatesModel


class CharityProject(DatesModel, Base):
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text, nullable=False)
    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, nullable=False, default=0)
    fully_invested = Column(Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'<CharityProject {vars(self)}>'