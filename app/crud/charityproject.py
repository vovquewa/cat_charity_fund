from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import CharityProject


class CRUDCharityProject(CRUDBase):
    async def get_id_by_name(
        self,
        charityproject_name: str,
        session: AsyncSession,

    ) -> Optional[int]:
        charityproject_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == charityproject_name
            )
        )
        charityproject_id = charityproject_id.scalars().first()
        return charityproject_id


charityproject_crud = CRUDCharityProject(CharityProject)