from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import history, user


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router, tags=["ユーザー系"])
app.include_router(history.router, tags=["決済履歴系"])

@app.get('/')
async def index():
    return {"status": "200 OK"}