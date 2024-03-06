from fastapi import APIRouter
from fastapi import APIRouter, Depends, status, Request, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.crud.masters import get_masters_service, get_master_by_id_service, create_master_service
from backend.app.database.database import get_db
from backend.app.schemas.master import MastersSchema

router = APIRouter()


@router.get('')
async def get_masters():
    result = await get_masters_service()
    return {"status code": "200", "status": "success", "content": result}


@router.get('/{id}')
async def get_master_by_id(master_id: int):
    result = await get_master_by_id_service(master_id)
    return {"status code": "200", "status": "success", "content": result}


@router.post('', status_code=status.HTTP_201_CREATED)
async def create_master(master: MastersSchema, request: Request, db_session: AsyncSession = Depends(get_db)):
    result = await create_master_service(master, request, db_session)
    return {"status code": "200", "status": "success", "content": result}
