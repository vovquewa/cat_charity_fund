from sqlalchemy import Boolean, Column, DateTime, Integer
from app.core.db import Base


class InvestmentModel(Base):
    __abstract__ = True

    create_date = Column(DateTime, nullable=False)
    close_date = Column(DateTime, nullable=True)
    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, nullable=False, default=0)
    fully_invested = Column(Boolean, nullable=False, default=False)

    def get_class_fields_and_values(self):
        return {
            k: v for k, v in self.__dict__.items() if (
                not k.startswith('_') and not callable(k)
            )
        }

    def __repr__(self):
        return (
            f'<{self.__class__.__name__} '
            f'{self.__class__.get_class_fields_and_values(self)}>'
        )