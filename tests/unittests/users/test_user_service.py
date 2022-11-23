import datetime

import pytest
from pydantic import EmailStr
from sqlalchemy.orm import Session

from general_types.typesafe_representations import Username
from sqlalchemymodels.connect_db import SessionFactory
from users.dtos.create_user_dto import CreateUserDTO
from users.exceptions.exeptions import UsernameTakenException
from users.repositories.abstract_user_repository import IUserRepository
from users.repositories.sql_user_repository import SQLUserRepository
from users.services.BasicUserService import BasicUserService
from users.services.IUserService import IUserService


@pytest.fixture(scope="function")
def make_user_service(get_injector):
    """Creates a session to share among all instances"""
    child_injector = get_injector.create_child_injector()
    child_injector.binder.bind(IUserRepository, SQLUserRepository)
    child_injector.binder.bind(IUserService, BasicUserService)
    session_factory = child_injector.get(SessionFactory)
    with session_factory() as session:
        session: Session
        child_injector.binder.bind(Session, session)
        yield session, child_injector.get(IUserService)
        session.commit()


def test_user_add_remove(subtests, make_user_service):
    session, user_service = make_user_service
    user_dto = CreateUserDTO(
        username=Username("JN98ZK"),
        birthdate=datetime.date(1998, 7, 14),
        email=EmailStr("Johnzakaria98@gmail.com"),
        first_name="John",
        last_name="Sorial",
    )

    with subtests.test(msg="Adding a tweets"):
        user_service.create_user(user_dto)

    with subtests.test(msg="Adding a tweets again should fail"):
        with pytest.raises(UsernameTakenException):
            user_service.create_user(user_dto)

    with subtests.test(msg="Deleting tweets should work"):
        user_service.delete_user(user_dto.username)
        user_service.create_user(user_dto)  # <- We can add him back
