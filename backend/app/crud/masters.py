from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, status, Request, HTTPException

from backend.app.database.database import get_db
from backend.app.models.master import Master
from backend.app.schemas.master import MastersSchema

masters = [{"id": 1, "name": "John", "second_name": "Wall", "sur_name": "Walich"}]


async def get_masters_service() -> list:
    return masters


async def get_master_by_id_service(master_id: int) -> dict:
    for master in masters:
        if master['id'] == master_id:
            return master


async def find_master_by_name(
        name: str,
        db_session: AsyncSession = Depends(get_db),
):
    return await Master.find(db_session, name)


async def create_master_service(master: MastersSchema, request: Request, db_session: AsyncSession = Depends(get_db)):
    _master: Master = Master(**master.model_dump())
    await _master.save(db_session)
    return _master
