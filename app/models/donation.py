from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy import ForeignKey

from app.core.db import Base


class Donation(Base):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text, nullable=True)
    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, nullable=False, default=0)
    fully_invested = Column(Boolean, nullable=False, default=False)
    create_date = Column(DateTime, nullable=False)
    close_date = Column(DateTime, nullable=True)
