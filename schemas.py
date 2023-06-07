import random
import time
from pydantic import BaseModel, Field
from datetime import datetime


class History(BaseModel):
    payment_id: str = Field(
        default=str(int(time.time() * 1000) + random.randint(0, 299)),
        description="決済ID(ランダムなIDが自動指定)",
    )
    class_name: str = Field(None, description="クラス名", example="2年1組")
    timestamp: str = Field(None, description="タイムスタンプ", example="2022-07-03 00:52:47")
    total: int = Field(None, description="購入金額", example=200)
    change: int = Field(None, description="お釣り", example=100)
    product: str = Field(None, description="購入商品", example="かき氷, 練乳")

    class Config:
        orm_mode = True


class Response_History(BaseModel):
    payment_id: str
    paid_class: str
    timestamp: datetime
    total: int
    change: int
    product: str

    class Config:
        orm_mode = True


class HistoryAdd(BaseModel):
    class_name: str = Field(None, description="クラス名", example="2年1組")
    total: int = Field(None, description="購入金額", example=200)
    change: int = Field(None, description="お釣り", example=100)
    product: str = Field(None, description="購入商品", example="かき氷, 練乳")

    class Config:
        orm_mode = True


class Response_User(BaseModel):
    user_mail: str
    user_name: str
    user_class: str
    user_role: str

    class Config:
        orm_mode = True


class User(BaseModel):
    user_role: str = Field("", description="管理者かどうか(管理者でない場合はNull)", example="Admin")
    user_mail: str = Field(
        None, description="生徒のメールアドレス", example="user@higashifukuoka.net"
    )
    user_name: str = Field(None, description="生徒氏名", example="徳野常道")
    user_class: str = Field(None, description="生徒所属クラス", example="1年1組")

    class Config:
        orm_mode = True
