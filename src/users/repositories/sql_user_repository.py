from typing import Optional

from injector import inject
from sqlalchemy import delete
from sqlalchemy import select
from sqlalchemy.orm import Session

from general_types.typesafe_representations import Username
from sqlalchemymodels.DBUserModel import DBUserModel
from users.dtos.create_user_dto import CreateUserDTO
from users.exceptions.exeptions import UsernameTakenException
from users.exceptions.exeptions import UserNotFoundException
from users.repositories.abstract_user_repository import IUserRepository


class SQLUserRepository(IUserRepository):
    @inject
    def __init__(self, session: Session):
        self.session = session

    def get_user(self, username: Username) -> DBUserModel:
        get_user_query = select(DBUserModel).where(DBUserModel.username == username)
        user: Optional[DBUserModel] = self.session.execute(
            get_user_query
        ).scalar_one_or_none()
        if user is None:
            raise UserNotFoundException()
        return user

    def is_username_available(self, username: Username) -> bool:
        username_query = select(DBUserModel.username).where(
            DBUserModel.username == username
        )
        return self.session.execute(username_query).scalar_one_or_none() is None

    def create_user(self, create_user_dto: CreateUserDTO):
        """
        Creates a user

        Args:
            create_user_dto: A representation of user data.

        Raises:
            UsernameTakenException: if a username is already taken.
        """

        if not self.is_username_available(create_user_dto.username):
            raise UsernameTakenException()

        user_db_model = DBUserModel(
            username=create_user_dto.username,
            email=create_user_dto.email,
            birthdate=create_user_dto.birthdate,
            first_name=create_user_dto.first_name,
            last_name=create_user_dto.last_name,
        )

        self.session.add(user_db_model)
        self.session.flush()

    def delete_user(self, username: Username):
        """
        Deletes a user

        Args:
            username: username to be deleted
        """
        self.session.execute(
            delete(DBUserModel).where(DBUserModel.username == username)
        )
