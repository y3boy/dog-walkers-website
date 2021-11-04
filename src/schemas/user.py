from pydantic import BaseModel, UUID4, Field, validator
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    username: str
    hashed_password: str
    fullname: str
    phone: str
    email: str


class TokenBase(BaseModel):
    token: UUID4 = Field(..., alias="access_token")
    expires: datetime
    token_type: Optional[str] = "bearer"

    class Config:
        allow_population_by_field_name = True
        orm_mode = True

    @validator("token")
    def hexlify_token(cls, value):
        return value.hex
