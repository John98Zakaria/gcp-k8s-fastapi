from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import declarative_base

BaseMetadata = declarative_base()


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, _):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
