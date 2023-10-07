from sqlalchemy import Column, ForeignKey, Integer, Text

from app.models.basefields import BaseFieldsModel


class Donation(BaseFieldsModel):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text, nullable=True)

    def __repr__(self):
        return (
            f'<Donation {self.id} {self.name} {self.description}, '
            f'{self.create_date}, {self.close_date}, {self.full_amount}, '
            f'{self.invested_amount}, {self.fully_invested}>'
        )
