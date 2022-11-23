from pathlib import Path

from pydantic import BaseSettings, Field


class SQlAlchemyConfiguration(BaseSettings):
    db_engine_str: str = Field(default="sqlite", env="db_engine_str")
    db_connection_str: str = Field(
        default="/../devdata/database.db", env="db_connection_str"
    )
    extra_db_params: str = Field(default="", env="extra_db_params")
    echo: bool = Field(
        default=False,
        description="Log SQL Queries to console",
        env="echo_db_statements",
    )

    @property
    def sql_alchemy_str(self):
        return f"{self.db_engine_str}://{self.db_connection_str}{self.extra_db_params}"


sql_config = SQlAlchemyConfiguration(extra_db_params="?check_same_thread=False")
if "sqlite" in sql_config.db_engine_str:  # Create Folder where database can live
    sql_path = Path(sql_config.db_connection_str[1:]).parent
    sql_path.mkdir(exist_ok=True, parents=True)
