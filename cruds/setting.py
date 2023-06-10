from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select, update
from typing import List, Optional, Tuple
import models


async def get_setting(db: AsyncSession, class_name: str) -> List[str]:
    stmt = select(models.GetAllSetting).where(models.Setting.class_name == class_name)
    result: Result = await db.execute(stmt)
    return result.scalar()


async def find_setting(db: AsyncSession, class_name: str) -> List[str]:
    stmt = select(models.GetAllSetting).where(models.Setting.class_name == class_name)
    result: Result = await db.execute(stmt)
    setting: Optional[Tuple[models.Settingx]] = result.first()
    return setting[0] if setting is not None else None


async def set_settings(
    class_name: str,
    goal: int,
    reserve: int,
    additionalreserve: int,
    db: AsyncSession,
):
    model = models.Setting
    existing_instance = await db.execute(
        select(model).where(model.class_name == class_name)
    )
    existing_instance = existing_instance.scalars().first()
    if existing_instance:
        await db.execute(
            update(model)
            .where(model.class_name == class_name)
            .values(goal=goal, reserve=reserve, additionalreserve=additionalreserve)
        )
    else:
        new_instance = model(
            class_name=class_name,
            goal=goal,
            reserve=reserve,
            additional=additionalreserve,
        )
        db.add(new_instance)
    await db.commit()
    if existing_instance:
        return existing_instance
    else:
        return new_instance
