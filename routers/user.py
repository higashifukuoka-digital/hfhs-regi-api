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
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import auth
import schemas

router = APIRouter()


@router.get("/user", response_model=schemas.Response_User)
async def get_userinfo(
    db: AsyncSession = Depends(get_db),
    authorization: HTTPAuthorizationCredentials = Depends(auth.get_current_user),
):
    response = await user_crud.get_user_info(db=db, user_mail=authorization["email"])
    if response is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"{authorization['email']} is not found."
        )
    return response
