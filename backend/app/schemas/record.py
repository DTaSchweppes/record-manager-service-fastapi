import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

config = ConfigDict(from_attributes=True)


class RecordSchema(BaseModel):
    id: Optional[int] = None
    id_client: Optional[int] = None
    id_service: Optional[int] = None
    id_master: Optional[int] = None
    time: Optional[datetime.datetime] = None


class RecordSchemaResponse(BaseModel):
    model_config = config
    id: UUID = Field(
        title="Id",
        description="",
    )
    id_client: UUID = Field(
        title="id client",
        description="",
    )
    id_service: UUID = Field(
        title="id service",
        description="",
    )
    id_master: UUID = Field(
        title="id master",
        description="",
    )
