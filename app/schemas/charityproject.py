from datetime import datetime, timedelta
from typing import Optional

from pydantic import BaseModel, Field

CREATE_DATE = (datetime.now() + timedelta(minutes=10)).isoformat(timespec='minutes')
CLOSE_DATE = (datetime.now() + timedelta(minutes=60)).isoformat(timespec='minutes')


class CharityProjectBase(BaseModel):
    name: str = Field(..., max_length=100)
    description: str
    full_amount: int = Field(..., gt=0)

    class Config:
        min_anystr_length = 1


class CharityProjectCreate(CharityProjectBase):
    pass


class CharityProjectUpdate(CharityProjectBase):
    name: Optional[str] = Field(None, max_length=100)
    description: Optional[str] = Field(None)
    full_amount: Optional[int] = Field(None, gt=0)

    class Config:
        extra = 'forbid'
        min_anystr_length = 1


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