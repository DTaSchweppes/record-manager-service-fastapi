from fastapi import APIRouter

from backend.app.crud.records import get_records_service, get_record_by_id_service, create_record_service
from backend.app.schemas.record import RecordSchema

router = APIRouter()


@router.get('')
async def get_records():
    result = await get_records_service()
    return {"status code": "200", "status": "success", "content": result}


@router.get('/{id}')
async def get_record_by_id(id_record: int):
    result = await get_record_by_id_service(id_record)
    return {"status code": "200", "status": "success", "content": result}


@router.post('')
async def create_record(record: RecordSchema):
    result = await create_record_service(record)
    return {"status code": "200", "status": "success", "content": result}
