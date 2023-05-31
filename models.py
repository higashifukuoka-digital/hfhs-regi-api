import datetime
import random
import time
from sqlalchemy import INTEGER, TIMESTAMP, Column, String, func
from db import Base
from datetime import datetime
import pytz
import random
import string

jst = pytz.timezone("Asia/Tokyo")


def generate_payment_id(length=16):
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=length))


class User(Base):
    __tablename__ = "users"

    user_mail = Column(String(31), primary_key=True)
    user_name = Column(String(20))
    user_class = Column(String(20))
    user_role = Column(String(20))


class History(Base):
    now = datetime.now(jst)
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    __tablename__ = "history"

    payment_id = Column(
        String(15),
        primary_key=True,
        default=str(generate_payment_id()),
    )
    paid_class = Column(String(16))
    timestamp = Column(TIMESTAMP, default=func.now())
    total = Column(INTEGER)
    change = Column(INTEGER)
    product = Column(String(255))

class Get_History_all(History):
    paid_class: str
    timestamp: str
    total: str
    change: str
    product: str

    class Config():
        orm_mode = True