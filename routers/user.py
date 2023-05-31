from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from db import get_db
from starlette.status import (
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
)
from sqlalchemy.ext.asyncio import AsyncSession
import cruds.user as user_crud

router = APIRouter()


@router.get("/user/{user_mail}")
async def get_userinfo(user_mail: str, db: AsyncSession = Depends(get_db)):
    response = await user_crud.get_user_info(db=db, user_mail=user_mail)
    if response is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{user_mail} is not found."
            )
    return response
