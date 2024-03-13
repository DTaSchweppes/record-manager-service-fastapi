from typing import Optional
from pydantic import BaseModel, Field, EmailStr
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class MastersSchema(BaseModel):
    id: Optional[int] = Field(..., description="master id")
    email: EmailStr = Field(title="User’s email", description="User’s email")
    first_name: str = Field(title="User’s first name", description="User’s first name")
    last_name: str = Field(title="User’s last name", description="User’s last name")