from pydantic import BaseSettings, Field


class KibanaConfig(BaseSettings):
    SERVICE_NAME: str = Field(..., env="KIBANA_SERVICE_NAME")
    SECRET_TOKEN: str = Field(..., env="KIBANA_SECRET_TOKEN")
    ENVIRONMENT: str = Field(..., env="KIBANA_ENVIRONMENT")
    SERVER_URL: str = Field(..., env="KIBANA_SERVER_URL")


kibana_config = KibanaConfig()
