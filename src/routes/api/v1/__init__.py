from fastapi import APIRouter

from src.routes.api.v1.health import health_router

__all__ = [
  "v1_router"
]

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(health_router)

