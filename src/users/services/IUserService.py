from abc import ABC
from abc import abstractmethod

from general_types.typesafe_representations import Username
from users.dtos.create_user_dto import CreateUserDTO


class IUserService(ABC):
    @abstractmethod
    def create_user(self, create_user_dto: CreateUserDTO):
        """
        Creates a user

        Args:
            create_user_dto: A representation of user data.

        Raises:
            UsernameTakenException: if a username is already taken.
        """
        pass

    @abstractmethod
    def delete_user(self, username: Username):
        """
        Deletes a user

        Args:
            username: username to be deleted
        """
        pass
