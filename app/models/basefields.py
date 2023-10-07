from sqlalchemy import Boolean, Column, DateTime, Integer
from app.core.db import Base


class BaseFieldsModel(Base):
    __abstract__ = True

    create_date = Column(DateTime, nullable=False)
    close_date = Column(DateTime, nullable=True)
    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, nullable=False, default=0)
    fully_invested = Column(Boolean, nullable=False, default=False)
