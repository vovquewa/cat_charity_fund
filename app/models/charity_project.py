from sqlalchemy import Boolean, Column, Integer, String, Text

from app.models.basetemplate import BaseTemplateModel


class CharityProject(BaseTemplateModel):
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text, nullable=False)

    def __repr__(self):
        return f'<CharityProject {vars(self)}>'