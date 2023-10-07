from sqlalchemy import Column, String, Text

from app.models.basefields import BaseFieldsModel


class CharityProject(BaseFieldsModel):
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text, nullable=False)

    def __repr__(self):
        return (
            f'<CharityProject {self.id} {self.name} {self.description}, '
            f'{self.create_date}, {self.close_date}, {self.full_amount}, '
            f'{self.invested_amount}, {self.fully_invested}>'
        )
