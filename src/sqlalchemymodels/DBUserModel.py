from pydantic import EmailStr
from sqlalchemy import Column

from general_types.typesafe_representations import Username
from sqlalchemymodels.auditing import SQLBase
from sqlalchemymodels.predifined_types import SQLUsernameStr, SQLNameStr, SQLEmailStr


def register_user_model():
    pass


class DBUserModel(SQLBase):
    __tablename__ = "users"
    username: Username = Column(SQLUsernameStr, primary_key=True)
    email: EmailStr = Column(SQLEmailStr, nullable=False, index=True)
    first_name: str = Column(SQLNameStr)
