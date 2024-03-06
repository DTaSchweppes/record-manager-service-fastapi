from backend.app.schemas.record import RecordSchema

records = [{"id": 1, "id_client": 1, "id_master": 1, "id_service": 1, "time": "2024 02 16"}]
masters = [{"id": 1, "name": "John", "second_name": "Wall", "dad_name": "Walich"}]


async def get_records_service() -> list:
    return records


async def get_record_by_id_service(record_id: int) -> dict:
    for record in records:
        if record['id'] == record_id:
            return record


async def create_record_service(record: RecordSchema) -> dict:
    records.append(record.dict())
    return record.dict()