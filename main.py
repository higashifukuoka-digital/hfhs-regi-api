from fastapi import Depends, FastAPI
from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials,
)
from fastapi.middleware.cors import CORSMiddleware
from routers import history, user, setting
import auth

key_scheme = HTTPBearer(
    description="Json Web Token with Encrypted", scheme_name="Token"
)

app = FastAPI()

origins = [
    "https://regi.hfhs-digital.app",
    "https://hfhs-registar.vercel.app",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router, tags=["ユーザー系"])
app.include_router(history.router, tags=["決済履歴系"])
app.include_router(setting.router, tags=["店舗設定系"])


@app.get("/", tags=["ステータス"])
async def index():
    return {"status": "200 OK"}

@app.get("/auth", tags=["認証系"])
async def get_islogin(
    authorization: HTTPAuthorizationCredentials = Depends(auth.get_current_user),
):
    return {"isLogin": authorization["email"]}
