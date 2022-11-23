from fastapi import APIRouter


k8s_health = APIRouter(tags=["Monitoring"])


@k8s_health.get("/readyz")
async def readyz():
    """
    Endpoint used for readiness probe

    """
    return True
