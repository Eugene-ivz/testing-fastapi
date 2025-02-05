from math import e
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import (AsyncAttrs,AsyncSession, async_sessionmaker,
                                    create_async_engine)
from typing import AsyncIterator

from app.config import settings

class Base(AsyncAttrs, DeclarativeBase):
    pass

DB_URL = settings.get_db_url()

engine = create_async_engine(DB_URL, echo=True)

async_session = async_sessionmaker(engine, expire_on_commit=False)

        
async def get_session() -> AsyncIterator[AsyncSession]:
    async with async_session() as session:
        yield session