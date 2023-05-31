from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from config import settings

DATABASE_URI = (
    "mysql+aiomysql://"
    + settings.mysql_user
    + ":"
    + settings.mysql_password
    + "@"
    + settings.db_host
    + "/"
    + settings.mysql_database
    + "?charset=utf8mb4"
)
engine = create_async_engine(
    DATABASE_URI, pool_size=3000, max_overflow=100, pool_timeout=3
)
async_session = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
)

Base = declarative_base()


async def get_db():
    async with async_session() as session:
        try:
            yield session
        except HTTPException as e:
            raise e
        except SQLAlchemyError as e:
            print(e)
            raise HTTPException(503, detail="Databse is slow.")
        except Exception as e:
            raise e
        finally:
            await session.close()
