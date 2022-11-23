from typing import Callable

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import Session, sessionmaker


class SessionFactory:
    def __init__(self, factory):
        self.factory = factory

    def __call__(self, *args, **kwargs):
        return self.factory


async def init_async_engine(engine_str: str, echo: bool = True):
    engine = create_async_engine(engine_str, echo=echo, future=True)
    return engine


def create_session_maker_async(engine: AsyncEngine) -> Callable[[], Session]:
    session_factory = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession, future=True
    )
    return session_factory


async def create_engine_async(sql_alchemy_str: str, echo: bool = False) -> AsyncEngine:
    return await init_async_engine(sql_alchemy_str, echo=echo)


def create_engine_sync(sql_alchemy_str: str, echo: bool = False) -> Engine:
    return create_engine(sql_alchemy_str, echo=echo)


def create_session_maker_sync(engine: Engine) -> Callable[[], Session]:
    session_factory = sessionmaker(engine, expire_on_commit=False, future=True)

    return session_factory
