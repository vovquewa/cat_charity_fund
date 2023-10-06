from sqlalchemy import Boolean, Column, ForeignKey, Integer, Text

from app.core.db import Base
from app.models.basetemplate import DatesModel


class Donation(DatesModel, Base):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text, nullable=True)
    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, nullable=False, default=0)
    fully_invested = Column(Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'<CharityProject {vars(self)}>'