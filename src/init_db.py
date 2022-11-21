from sqlalchemy.engine import Engine
from sqlalchemy.ext.asyncio import AsyncEngine

from backend_conf import sql_config
from sqlalchemymodels import BaseMetadata
from sqlalchemymodels.connect_db import create_engine_sync
from sqlalchemymodels.model_registry import register_sql_models


async def create_db_async(engine: AsyncEngine):
    async with engine.begin() as conn:
        await conn.run_sync(BaseMetadata.metadata.create_all)


def create_db_sync(engine: Engine):
    BaseMetadata.metadata.create_all(engine)


print(f"{sql_config.sql_alchemy_str}=")
if __name__ == '__main__':
    register_sql_models()
    sync_engine = create_engine_sync(sql_config.sql_alchemy_str, echo=True)
    create_db_sync(sync_engine)
