# Model is the representation of my table witch means it's equal to the database

from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base


class ProductModels(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    category = Column(String)
    email_seller = Column(String)
    created_at = Column(DateTime(timezone=True), default=func.now())
