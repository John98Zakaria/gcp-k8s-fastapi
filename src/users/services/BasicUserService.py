from injector import inject

from general_types.typesafe_representations import Username
from sqlalchemymodels.DBUserModel import DBUserModel
from users.dtos.create_user_dto import CreateUserDTO
from users.repositories.abstract_user_repository import IUserRepository
from users.services.IUserService import IUserService


class BasicUserService(IUserService):
    @inject
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    def get_user(self, username: Username) -> DBUserModel:
        return self.user_repo.get_user(username)

    def create_user(self, create_user_dto: CreateUserDTO):
        self.user_repo.create_user(create_user_dto)

    def delete_user(self, username: Username):
        self.user_repo.delete_user(username)
