import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    mysql_database: str = os.getenv("MYSQL_DATABASE")
    mysql_user: str = os.getenv("MYSQL_USER")
    mysql_password: str = os.getenv("MYSQL_PASSWORD")
    db_host: str = "mysql_host"
    jwt_secret: str = os.getenv("JWT_SECRET")

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
