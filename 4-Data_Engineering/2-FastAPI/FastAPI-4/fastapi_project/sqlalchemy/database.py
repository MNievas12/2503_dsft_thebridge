from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from fastapi_project.sqlalchemy.models import Base

DATABASE_URL = "sqlite+aiosqlite:///fastapi_sqlalchemy.db"


# the engine is an object that will manage the connection to the database
engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(
    engine, expire_on_commit=False
)  # this returns a function to generate sessions


# each HTTP request yields a fresh session that is closed when the request is answered
# That's why we need a generator

# *with* keyword is a context manager
# objects that need a setup logic before being used and a teardown logic when they are not used anymore
# like when we want to open a file, write and close the file

# *yield* keyword makes sure that the session remains open till the end of the request
# *return* would close immediately

# get_async_session is a dependency, FastAPI makes it very easy to swap it with another function
# this is helpful for testing!


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


# we will create all the tables in the beginning
# simple approach but enough for our goal


async def create_all_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
