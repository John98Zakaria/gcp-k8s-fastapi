from fastapi import APIRouter

k8s_health = APIRouter(prefix="/")


@k8s_health.get("/readyz")
async def readyz():
    return True
