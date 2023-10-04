from typing import Optional
from datetime import datetime, timedelta

from pydantic import BaseModel, root_validator, validator, Field

CREATE_DATE = (datetime.now() + timedelta(minutes=10)).isoformat(timespec='minutes')
CLOSE_DATE = (datetime.now() + timedelta(minutes=60)).isoformat(timespec='minutes')


class CharityProjectBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1)
    full_amount: int = Field(..., gt=0)


class CharityProjectCreate(CharityProjectBase):
    pass


class CharityProjectUpdate(CharityProjectBase):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, min_length=1)
    full_amount: Optional[int] = Field(None, gt=0)

    class Config:
        extra = 'forbid'


class CharityProjectCreateDB(CharityProjectBase):
    id: int
    invested_amount: int = Field(0, ge=0)
    fully_invested: bool = Field(False, example=True)
    create_date: datetime = Field(..., example=CREATE_DATE)
    close_date: Optional[datetime] = Field(..., example=CLOSE_DATE)

    class Config:
        orm_mode = True


class CharityProjectDB(CharityProjectBase):
    id: int
    invested_amount: int = Field(0, ge=0)
    fully_invested: bool = Field(False, example=True)
    create_date: datetime = Field(..., example=CREATE_DATE)
    close_date: Optional[datetime] = Field(..., example=CLOSE_DATE)

    class Config:
        orm_mode = True