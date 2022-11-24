from functools import partial

from fastapi import Depends, Response
from fastapi_restful.cbv import cbv
from fastapi_restful.inferring_router import InferringRouter
from starlette import status

from dependency_injection import Injection
from general_types.general_responses import BasicResponse
from general_types.typesafe_representations import Username
from users.dtos.create_user_dto import CreateUserDTO
from users.dtos.user_response_model import UserResponse
from users.exceptions.exeptions import UsernameTakenException
from users.services.IUserService import IUserService

users_router = InferringRouter(prefix="/users", tags=["Users"])


@cbv(users_router)
class UsersAPI:
    data_service: IUserService = Depends(partial(Injection.db_session, IUserService))

    @users_router.post(
        "/sign-up",
        status_code=status.HTTP_201_CREATED,
        responses={status.HTTP_412_PRECONDITION_FAILED: {"model": BasicResponse}},
    )
    def sign_up(
        self, create_user_dto: CreateUserDTO, response: Response
    ) -> BasicResponse:
        try:
            self.data_service.create_user(create_user_dto)
            # https://www.rfc-editor.org/rfc/rfc7231#section-6.3.2
            response.status_code = status.HTTP_201_CREATED
            response.headers["Location"] = f"/users/{create_user_dto.username}"
            return BasicResponse(msg="Created Successfully")
        except UsernameTakenException:
            response.status_code = status.HTTP_412_PRECONDITION_FAILED
            return BasicResponse(msg="Username was already Taken")

    @users_router.get("/{username}")
    def get_user_profile(self, username: Username) -> UserResponse:
        user = self.data_service.get_user(username)

        return UserResponse.from_orm(user)

    @users_router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
    def delete_user(self, username: Username):
        pass
