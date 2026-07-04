from fastapi import APIRouter

health_router = APIRouter(prefix="/health", tags=["Health Check"])

@health_router.get("/")
def health_check():
  return {
    "status": "working",
  }

