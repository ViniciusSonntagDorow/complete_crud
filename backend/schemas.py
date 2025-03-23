# Schema is the representation of my user's interaction

from pydantic import BaseModel, PositiveFloat, EmailStr
from datetime import datetime
from typing import Optional


class ProdutsBase(BaseModel):
    name: str
    description: str
    price: PositiveFloat
    category: str
    email_seller: EmailStr


class ProductCreate(ProdutsBase):
    pass


class ProductResponse(ProdutsBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class ProductUpdate(ProdutsBase):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[PositiveFloat] = None
    category: Optional[str] = None
    email_seller: Optional[EmailStr] = None
