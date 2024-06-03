from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select
from typing import List
import models


async def get_all_history(db: AsyncSession, class_name: str) -> List[str]:
    stmt = select(
        models.GetHistoryAll,
    ).where(models.History.paid_class == class_name)
    result: Result = await db.execute(stmt)
    result = result.all()
    return [record[0].__dict__ for record in result]


async def add_order(
    payment_id: str,
    class_name: str,
    total: int,
    change: int,
    product: str,
    db: AsyncSession,
):
    model = models.History
    instance = model(
        payment_id=payment_id,
        paid_class=class_name,
        total=total,
        change=change,
        product=product,
    )
    db.add(instance)
    await db.commit()
    await db.refresh(instance)
    return instance
