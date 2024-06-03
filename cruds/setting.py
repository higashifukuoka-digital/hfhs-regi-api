from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select, update
from typing import Optional
import models

async def get_setting(db: AsyncSession, class_name: str) -> Optional[models.Setting]:
    stmt = select(models.Setting).where(models.Setting.class_name == class_name)
    result: Result = await db.execute(stmt)
    setting: Optional[models.Setting] = result.scalars().first()
    return setting

async def find_setting(db: AsyncSession, class_name: str) -> Optional[models.Setting]:
    stmt = select(models.Setting).where(models.Setting.class_name == class_name)
    result: Result = await db.execute(stmt)
    setting: Optional[models.Setting] = result.scalars().first()
    return setting

async def set_settings(
    class_name: str,
    goal: int,
    reserve: int,
    additionalreserve: int,
    db: AsyncSession,
) -> models.Setting:
    stmt = select(models.Setting).where(models.Setting.class_name == class_name)
    result: Result = await db.execute(stmt)
    existing_instance: Optional[models.Setting] = result.scalars().first()

    if existing_instance:
        await db.execute(
            update(models.Setting)
            .where(models.Setting.class_name == class_name)
            .values(goal=goal, reserve=reserve, additionalreserve=additionalreserve)
        )
    else:
        new_instance = models.Setting(
            class_name=class_name,
            goal=goal,
            reserve=reserve,
            additionalreserve=additionalreserve,
        )
        db.add(new_instance)
    await db.commit()
    return existing_instance if existing_instance else new_instance

