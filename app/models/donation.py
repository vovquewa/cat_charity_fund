from sqlalchemy import Column, ForeignKey, Integer, Text

from app.models.basetemplate import BaseTemplateModel


class Donation(BaseTemplateModel):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text, nullable=True)

    def __repr__(self):
        return f'<CharityProject {vars(self)}>'