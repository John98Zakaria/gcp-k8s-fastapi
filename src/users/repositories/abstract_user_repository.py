from abc import ABC, abstractmethod

from general_types.typesafe_representations import Username
from sqlalchemymodels.DBUserModel import DBUserModel
from users.dtos.create_user_dto import CreateUserDTO


class IUserRepository(ABC):
    @abstractmethod
    def create_user(self, create_user_dto: CreateUserDTO):
        """
        Creates a tweets

        Args:
            create_user_dto: A representation of tweets data.

        Raises:
            UsernameTakenException: if a username is already taken.
        """
        pass

    @abstractmethod
    def get_user(self, username: Username) -> DBUserModel:
        """
        Gets a tweets from the database

        Args:
            username: username
        Returns:
            User if found
        Raises:
            UserNotFoundException: If tweets is not found
        """
        pass

    @abstractmethod
    def delete_user(self, username: Username):
        """
        Deletes a tweets

        Args:
            username: username to be deleted
        """
        pass
