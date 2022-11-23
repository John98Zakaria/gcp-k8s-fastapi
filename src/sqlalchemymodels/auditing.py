import datetime

from sqlalchemy import TIMESTAMP, Column, Integer, text

from sqlalchemymodels import BaseMetadata


class SQLBase(BaseMetadata):
    """"""

    __abstract__ = True

    created_on: datetime.datetime = Column(
        TIMESTAMP, default=datetime.datetime.utcnow, nullable=False
    )
    updated_on: datetime.datetime = Column(
        TIMESTAMP,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        nullable=False,
    )

    version: int = Column(
        Integer,
        default=1,
        nullable=False,
        server_default=text("1"),
        server_onupdate=text("version + 1"),
    )
