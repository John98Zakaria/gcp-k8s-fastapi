from elasticapm.contrib.starlette import ElasticAPM, make_apm_client
from fastapi import FastAPI

from kibana_monitoring.kibana_config import kibana_config


def setup_kibana(app: FastAPI):
    kibana_apm = make_apm_client(kibana_config.dict())
    app.add_middleware(ElasticAPM, client=kibana_apm)
