import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    mysql_database: str = os.getenv("MYSQL_DATABASE")
    mysql_user: str = os.getenv("MYSQL_USER")
    mysql_password: str = os.getenv("MYSQL_PASSWORD")
    db_host: str = "mysql_host"

    class Config:
        env_file = ".env"


settings = Settings()