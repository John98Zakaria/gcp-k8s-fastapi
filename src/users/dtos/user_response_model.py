import datetime

from pydantic import BaseModel
from pydantic import EmailStr

from general_types.typesafe_representations import Username


class UserResponse(BaseModel):
    username: Username
    email: EmailStr
    birthdate: datetime.date
    first_name: str
    last_name: str

    class Config:
        orm_mode = True
