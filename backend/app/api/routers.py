from fastapi import APIRouter
from backend.app.api.v1.masters.masters import router as masters_router
from backend.app.api.v1.records.records import router as records_router

v1 = APIRouter()

v1.include_router(masters_router, prefix='/masters')
v1.include_router(records_router, prefix='/records')
