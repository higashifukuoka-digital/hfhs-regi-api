from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
import cruds.setting as setting_crud
import cruds.user as user_crud
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import auth
import schemas

router = APIRouter()


@router.get("/setting/{class_name}", response_model=schemas.Response_Setting)
async def get_setting(
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
        response = await setting_crud.get_setting(db=db, class_name=class_name)
        if not response:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"{class_name} is not found.",
            )
        return response


@router.post("/setting/set/{class_name}", response_model=schemas.Setting)
async def set_setting(
    class_name: str,
    goal: int,
    reserve: int,
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
        await setting_crud.set_settings(class_name, goal, reserve, db)
        raise HTTPException(status_code=status.HTTP_200_OK, detail="Recorded")
