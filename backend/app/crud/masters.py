from backend.app.schemas.master import MastersSchema
from backend.app.schemas.record import RecordSchema

masters = [{"id": 1, "name": "John", "second_name": "Wall", "sur_name": "Walich"}]


async def get_masters_service() -> list:
    return masters


async def get_master_by_id_service(master_id: int) -> dict:
    for master in masters:
        if master['id'] == master_id:
            return master


async def create_master_service(master: MastersSchema) -> dict:
    masters.append(master.dict())
    return master.dict()
