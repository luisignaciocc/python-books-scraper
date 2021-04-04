from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from src.models.base import Base

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer(), primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    url = Column(String(100), nullable=False, unique=True)
    created_at = Column(DateTime(), default=func.current_timestamp())
    updated_at = Column(DateTime(), nullable=True)
    books = relationship("Book", back_populates="category")