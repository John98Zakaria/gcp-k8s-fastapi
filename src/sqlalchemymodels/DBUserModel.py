import datetime
import uuid
from typing import List

from pydantic import EmailStr
from sqlalchemy import Column, ForeignKey, func, text, select
from sqlalchemy import DateTime
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship, column_property
from sqlalchemy_utils import UUIDType

from general_types.typesafe_representations import Username, GID
from sqlalchemymodels.auditing import SQLBase
from sqlalchemymodels.predifined_types import SQLNameStr, SQLEmailStr, TweetStr
from sqlalchemymodels.predifined_types import SQLUsernameStr


def register_user_model():
    pass


class DBTweetModel(SQLBase):
    __tablename__ = "tweets"
    tweet_id: GID = Column(UUIDType, default=lambda: str(uuid.uuid4()), primary_key=True)
    creator: Username = Column(SQLUsernameStr, ForeignKey("users.username", ondelete="cascade", ), nullable=False,
                               index=True)

    tweet_content: str = Column(TweetStr, nullable=False)


class DBUserModel(SQLBase):
    __tablename__ = "users"
    username: Username = Column(SQLUsernameStr, primary_key=True)
    email: EmailStr = Column(SQLEmailStr, nullable=False, index=True)
    birthdate: datetime.date = Column(DateTime, nullable=False)
    first_name: str = Column(SQLNameStr, nullable=False)
    last_name: str = Column(SQLNameStr, nullable=False)
    tweets: List["DBTweetModel"] = relationship("DBTweetModel", uselist=True, passive_deletes=True,
                                                cascade="all, delete-orphan")

    num_tweets = column_property(
        select(func.count(text("tweet_id"))).where(DBTweetModel.creator == username).scalar_subquery())

    ## Hybrid_properties are evaluated lazily
    @hybrid_property
    def num_tweets_hybrid(self):
        if self.tweets:
            return len(self.tweets)
        return 0

    @num_tweets_hybrid.expression
    def num_tweets_expr(cls):
        return select(func.count(DBTweetModel.tweet_id)).where(DBTweetModel.creator == cls.username)

    @property
    def fullname(self):
        return self.first_name + " " + self.last_name

    @property
    def age(self):
        return datetime.datetime.utcnow().year - self.birthdate.year
