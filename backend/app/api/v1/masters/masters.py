from fastapi import APIRouter

from backend.app.crud.masters import get_masters_service, get_master_by_id_service, create_master_service
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


@router.post('')
async def create_master(master: MastersSchema):
    result = await create_master_service(master)
    return {"status code": "200", "status": "success", "content": result}
