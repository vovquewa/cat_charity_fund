from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Text

from app.core.db import Base
from app.models.dates import DatesModel


class Donation(DatesModel, Base):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text, nullable=True)
    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, nullable=False, default=0)
    fully_invested = Column(Boolean, nullable=False, default=False)
    # create_date = Column(DateTime, nullable=False)
    # close_date = Column(DateTime, nullable=True)
