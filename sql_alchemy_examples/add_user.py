import datetime

from sqlalchemy import select

from backend_conf import sql_config
from sqlalchemymodels.connect_db import create_engine_sync, create_session_maker_sync
from sqlalchemymodels.DBUserModel import DBTweetModel, DBUserModel


sync_engine = create_engine_sync(sql_config.sql_alchemy_str, True)
session_maker = create_session_maker_sync(sync_engine)

tweets = DBUserModel(
    username="JN98ZK2",
    email="johnzakaria98@gmail.com",
    birthdate=datetime.date(1998, 7, 14),
    first_name="John",
    last_name="Sorial",
)

tweet1 = DBTweetModel(creator="JN98ZK2", tweet_content="I like trains")
tweet2 = DBTweetModel(creator="JN98ZK2", tweet_content="I like food")

user_query = select(DBTweetModel).where(DBTweetModel.creator == "JN98ZK2")

with session_maker() as session:
    tweets: list[DBTweetModel] = session.execute(user_query).scalars().all()

    for tweet in tweets:
        print(tweet.tweet_content)

    # # print(f"{tweets.tweets}")
    # session.add(tweets)
    # session.add(tweet1)
    # session.add(tweet2)
    #
    session.commit()
