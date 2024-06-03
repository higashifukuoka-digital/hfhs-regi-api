from datetime import datetime
import random
from sqlalchemy import INTEGER, TIMESTAMP, String, func
from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from pydantic import BaseModel
import pytz
import string

Base = declarative_base()
jst = pytz.timezone("Asia/Tokyo")

def generate_payment_id(length=16):
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=length))

class User(Base):
    __tablename__ = "users"

    user_mail: Mapped[str] = mapped_column(String(31), primary_key=True)
    user_name: Mapped[str] = mapped_column(String(20))
    user_class: Mapped[str] = mapped_column(String(20))
    user_role: Mapped[str] = mapped_column(String(20))

class Setting(Base):
    __tablename__ = "setting"

    class_name: Mapped[str] = mapped_column(String(10), primary_key=True)
    goal: Mapped[int] = mapped_column(INTEGER)
    reserve: Mapped[int] = mapped_column(INTEGER)
    additionalreserve: Mapped[int] = mapped_column(INTEGER)

class History(Base):
    now = datetime.now(jst)
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    __tablename__ = "history"

    payment_id: Mapped[str] = mapped_column(String(15), primary_key=True, default=generate_payment_id)
    paid_class: Mapped[str] = mapped_column(String(16))
    timestamp: Mapped[datetime] = mapped_column(TIMESTAMP, default=func.now())
    total: Mapped[int] = mapped_column(INTEGER)
    change: Mapped[int] = mapped_column(INTEGER)
    product: Mapped[str] = mapped_column(String(255))

class GetAllSetting(BaseModel):
    class_name: str
    goal: int
    reserve: int
    additionalreserve: int

    class Config:
        orm_mode = True
        from_attributes = True

class GetAllHistory(BaseModel):
    payment_id: str
    paid_class: str
    timestamp: datetime
    total: int
    change: int
    product: str

    class Config:
        orm_mode = True
        from_attributes = True
