import datetime

from pydantic import BaseModel
from pydantic import EmailStr

from general_types.typesafe_representations import Username


class CreateUserDTO(BaseModel):
    username: Username
    birthdate: datetime.date
    email: EmailStr
    first_name: str
    last_name: str
