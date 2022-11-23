from pydantic import BaseModel


class BasicResponse(BaseModel):
    msg: str
