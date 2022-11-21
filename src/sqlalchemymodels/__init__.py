from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base

BaseMetadata = declarative_base()


async def init_async_engine(engine_str: str, echo: bool = True):
    engine = create_async_engine(engine_str, echo=echo, future=True)
    return engine


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, _):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
