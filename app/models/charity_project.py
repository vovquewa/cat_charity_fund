from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text

from app.core.db import Base


class CharityProject(Base):
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text, nullable=False)
    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, nullable=False, default=0)
    fully_invested = Column(Boolean, nullable=False, default=False)
    create_date = Column(DateTime, nullable=False)
    close_date = Column(DateTime, nullable=True)
