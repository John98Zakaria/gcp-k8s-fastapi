import datetime

from sqlalchemy import select

from backend_conf import sql_config
from sqlalchemymodels.DBUserModel import DBUserModel, DBTweetModel
from sqlalchemymodels.connect_db import create_engine_sync, create_session_maker_sync

sync_engine = create_engine_sync(sql_config.sql_alchemy_str, True)
session_maker = create_session_maker_sync(sync_engine)

user = DBUserModel(username="JN98ZK",
                   email="johnzakaria98@gmail.com",
                   birthdate=datetime.date(1998, 7, 14),
                   first_name="John",
                   last_name="Sorial")

tweet1 = DBTweetModel(
    creator="JN98ZK",
    tweet_content="I like trains"
)
tweet2 = DBTweetModel(
    creator="JN98ZK",
    tweet_content="I like food"
)

user_query = select(DBUserModel).where(DBUserModel.username == "JN98ZK")

with session_maker() as session:
    user: DBUserModel = session.execute(user_query).scalar()
    # print(f"{user.tweets}")
    # session.add(user)
    # session.add(tweet1)
    # session.add(tweet2)
    #
    session.commit()
