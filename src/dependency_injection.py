from typing import TypeVar, Type, Callable

from config import dev_config
from datastoreage.repository.abstract_blobstore import IBlobStore
from datastoreage.repository.abstract_tracker import AbstractDataRepository
from datastoreage.repository.alchemy_repository import DataRepositorySQL
from datastoreage.repository.file_blobstore import FileBlobStore
from init_db import create_session_maker_sync, create_engine_sync, SessionFactory
from injector import Injector, singleton
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session
from validation.services.celery_validation_service import CeleryValidationService

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
        engine = create_engine_sync(dev_config.sqlalchemy_str)
        injector.binder.bind(Engine, engine, scope=singleton)
        async_session_factory: Callable[[], Session] = create_session_maker_sync(engine)
        injector.binder.bind(SessionFactory, async_session_factory)
        injector.binder.bind(
            IBlobStore, FileBlobStore(dev_config.data_store_path), scope=singleton
        )
        injector.binder.bind(AbstractDataRepository, DataRepositorySQL)
        injector.binder.bind(CeleryValidationService, CeleryValidationService)
