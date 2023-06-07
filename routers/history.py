import random
import string
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
import cruds.history as history_crud
import cruds.user as user_crud
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import auth
import schemas

router = APIRouter()


def generate_payment_id(length=16):
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=length))


@router.get("/history/{class_name}", response_model=List[schemas.Response_History])
async def get_all_history(
    class_name: str,
    db: AsyncSession = Depends(get_db),
    authorization: HTTPAuthorizationCredentials = Depends(auth.get_current_user),
):
    user_class = await user_crud.get_user_info(db=db, user_mail=authorization["email"])
    if user_class is []:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can't access this endpoint.",
        )
    else:
        response = await history_crud.get_all_history(db=db, class_name=class_name)
        if not response:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"{class_name} is not found.",
            )
        return response


@router.post("/history/add/{class_name}", response_model=schemas.HistoryAdd)
async def add_history(
    class_name: str,
    change: int,
    total: int,
    product: str,
    db: AsyncSession = Depends(get_db),
    authorization: HTTPAuthorizationCredentials = Depends(auth.get_current_user),
):
    user_class = await user_crud.get_user_info(db=db, user_mail=authorization["email"])
    if user_class is []:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can't access this endpoint.",
        )
    else:
        await history_crud.add_order(
            generate_payment_id(), class_name, change, total, product, db
        )
        raise HTTPException(status_code=status.HTTP_200_OK, detail="Recorded")
