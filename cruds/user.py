from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select
from typing import List
import models


async def get_user_info(db: AsyncSession, user_mail: str) -> List[str]:
    stmt = select(models.User).where(models.User.user_mail == user_mail)
    result: Result = await db.execute(stmt)
    return result.scalar()