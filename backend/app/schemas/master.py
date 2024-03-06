from typing import Optional
from pydantic import BaseModel, Field


class MastersSchema(BaseModel):
    id: Optional[int] = Field(..., description="master id")
    name: Optional[str] = Field(..., description="Name")
    second_name: Optional[str] = Field(..., description="Second name")
    sur_name: Optional[str] = Field(..., description="Surname ")