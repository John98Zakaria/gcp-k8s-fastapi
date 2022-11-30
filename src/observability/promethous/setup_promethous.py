from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator


def setup_prometheus(app: FastAPI):
    Instrumentator().instrument(app).expose(app, include_in_schema=True)
