from datetime import datetime, timedelta
from typing import Optional

from pydantic import BaseModel, Field

CREATE_DATE = (datetime.now() + timedelta(minutes=10)).isoformat(timespec='minutes')
CLOSE_DATE = (datetime.now() + timedelta(minutes=60)).isoformat(timespec='minutes')


class DonationBase(BaseModel):
    comment: Optional[str]


class DonationCreate(DonationBase):
    full_amount: int = Field(..., gt=0)


class DonationDBPostGetMy(DonationBase):
    id: int
    full_amount: int
    create_date: datetime

    class Config:
        orm_mode = True


class DonationDB(DonationBase):
    id: int
    user_id: int
    comment: Optional[str]
    full_amount: int = Field(..., gt=0)
    invested_amount: int = Field(0, ge=0)
    fully_invested: bool = Field(False, example=True)
    create_date: datetime = Field(..., example=CREATE_DATE)
    close_date: Optional[datetime] = Field(..., example=CLOSE_DATE)

    class Config:
        orm_mode = True