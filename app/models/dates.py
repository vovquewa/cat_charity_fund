from sqlalchemy import Column, DateTime


class DatesModel:
    create_date = Column(DateTime, nullable=False)
    close_date = Column(DateTime, nullable=True)
