from typing import Optional
from pydantic import BaseModel, Field, EmailStr
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class MastersSchema(BaseModel):
    email: EmailStr = Field(title="Master’s email", description="master email")
    first_name: str = Field(title="Master’s first name", description="master first name")
    last_name: str = Field(title="Master’s last name", description="master last name")
    surname: str = Field(title="Master's surname", description="master surname")
