from fastapi import APIRouter

from app.api.endpoints import tron_router

main_router = APIRouter(prefix="/api/v1")
main_router.include_router(tron_router, prefix="/tron", tags=["Tron"])
