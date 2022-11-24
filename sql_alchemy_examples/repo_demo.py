import datetime

from pydantic import EmailStr

from backend_conf import sql_config
from general_types.typesafe_representations import Username
from sqlalchemymodels.connect_db import create_engine_sync, create_session_maker_sync
from users.dtos.create_user_dto import CreateUserDTO
from users.repositories.sql_user_repository import SQLUserRepository

sync_engine = create_engine_sync(sql_config.sql_alchemy_str, True)
session_maker = create_session_maker_sync(sync_engine)
with session_maker() as session:
    repo = SQLUserRepository(session)
    repo.create_user(
        CreateUserDTO(
            username=Username("JN98ZK"),
            birthdate=datetime.date(1998, 7, 14),
            email=EmailStr("John98zakaria@gmail.com"),
            first_name="John",
            last_name="Sorial",
        )
    )
