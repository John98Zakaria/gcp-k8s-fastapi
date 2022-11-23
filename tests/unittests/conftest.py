"""
This defines test fixtures that can be shared across tests
"""
import asyncio
from pathlib import Path
from typing import Callable

import pytest
from injector import singleton
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from dependency_injection import injector
from init_db import create_db_async, create_db_sync
from sqlalchemymodels.connect_db import (
    SessionFactory,
    create_engine_async,
    create_engine_sync,
    create_session_maker_sync,
)


TEST_ROOT = Path(__file__).parent.parent


@pytest.fixture(scope="class")
def event_loop():
    return asyncio.get_event_loop()


@pytest.fixture(scope="session")
def get_injector():
    engine = make_testing_database_engine_sync()
    injector.binder.bind(Engine, engine, scope=singleton)
    sync_session_factory: Callable[[], Session] = create_session_maker_sync(engine)
    injector.binder.bind(SessionFactory, sync_session_factory)
    return injector


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, _):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


def make_testing_database_engine_sync():
    engine = create_engine_sync("sqlite://")
    # engine = create_engine_sync("sqlite:///testing.db")
    create_db_sync(engine)
    return engine


async def make_testing_database_engine_async():
    engine = await create_engine_async("sqlite+aiosqlite://")
    # engine = await create_engine_async("sqlite+aiosqlite:///testing.db")
    await create_db_async(engine)

    return engine
