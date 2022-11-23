from fastapi import FastAPI

from dependency_injection import Injection
from health.k8s_health import k8s_health
from kibana_monitoring.setup_kibana import setup_kibana
from users.controllers.users_web import users_router

app = FastAPI()


@app.on_event("startup")
def startup_setup():
    setup_kibana(app)
    Injection.inject()
    app.include_router(k8s_health)
    app.include_router(users_router)


@app.get("/")
async def get_hello_server() -> str:
    return "Welcome to John's Sever"
