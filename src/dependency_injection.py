from typing import Callable, Type, TypeVar

from injector import Injector, singleton
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from backend_conf import sql_config
from sqlalchemymodels.connect_db import (
    SessionFactory,
    create_engine_sync,
    create_session_maker_sync,
)
from users.repositories.abstract_user_repository import IUserRepository
from users.repositories.sql_user_repository import SQLUserRepository
from users.services.BasicUserService import BasicUserService
from users.services.IUserService import IUserService


T = TypeVar("T")
injector = Injector()


class Injection:
    @staticmethod
    def on(dependency_class: Type[T]) -> Callable[[], T]:
        """Bridge between FastAPI injection and 'injector' DI framework."""
        return lambda: injector.get(dependency_class)

    @staticmethod
    def db_session(dependency_class: Type[T]) -> Callable[[], T]:
        """Creates a session to share among all instances"""
        child_injector = injector.create_child_injector()
        session_factory = injector.get(SessionFactory)
        with session_factory() as session:
            session: Session
            child_injector.binder.bind(Session, session)
            yield child_injector.get(dependency_class)
            session.commit()

    @staticmethod
    def inject():
        engine = create_engine_sync(sql_config.sql_alchemy_str)
        injector.binder.bind(Engine, engine, scope=singleton)
        sync_session_factory: Callable[[], Session] = create_session_maker_sync(engine)
        injector.binder.bind(SessionFactory, sync_session_factory)
        injector.binder.bind(IUserRepository, SQLUserRepository)
        injector.binder.bind(IUserService, BasicUserService)
