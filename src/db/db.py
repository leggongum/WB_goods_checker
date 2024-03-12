from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from config import settings

engine = create_async_engine(
    url=settings.DB_URL_SQLite,
)

class Base(DeclarativeBase):
    pass


session_factory = async_sessionmaker(engine)
