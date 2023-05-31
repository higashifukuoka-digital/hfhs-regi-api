import random
import string
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
import schemas
from db import get_db
from sqlalchemy.orm import Session
from starlette.status import (
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
)
from sqlalchemy.ext.asyncio import AsyncSession
import cruds.history as history_crud

router = APIRouter()


def generate_payment_id(length=16):
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=length))


@router.get("/history/{class_name}")
async def get_all_history(class_name: str, db: AsyncSession = Depends(get_db)):
    response = await history_crud.get_all_history(db=db, class_name=class_name)
    if response is []:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"{class_name} is not found."
        )
    return response


@router.post("/history/add/{class_name}")
async def add_history(
    class_name: str,
    change: int,
    total: int,
    product: str,
    db: AsyncSession = Depends(get_db),
):
    await history_crud.add_order(generate_payment_id(), class_name, change, total, product, db)
    return "正常にデータが保存できました。"
