import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from app.db.base import Base, get_session
from app.main import app
from app.config import settings

TEST_DATABASE = settings.get_db_url()


@pytest.fixture(scope="session")
def async_engine():
    return create_async_engine(TEST_DATABASE, poolclass=NullPool, echo=True)

@pytest.fixture(scope="session")
def async_session_factory(async_engine):
    return async_sessionmaker(async_engine, expire_on_commit=False)

@pytest.fixture(scope="session", autouse=True)
async def setup_database(async_engine):
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.fixture
async def db_session(async_session_factory):
    async with async_session_factory() as session:
        yield session

@pytest.fixture(scope="session")
async def async_client():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as client:
        yield client

@pytest.fixture(scope="session", autouse=True)
async def override_dependency(async_session_factory):
    async def _get_session():
        async with async_session_factory() as session:
            yield session

    app.dependency_overrides[get_session] = _get_session
    yield
    app.dependency_overrides.clear()