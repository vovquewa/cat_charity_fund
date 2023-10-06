from sqlalchemy import Column, DateTime
from app.core.db import Base


class DatesModel:
    create_date = Column(DateTime, nullable=False)
    close_date = Column(DateTime, nullable=True)
