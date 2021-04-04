from sqlalchemy import Table, Column, Integer, Numeric, ForeignKey, String, DateTime, func
from sqlalchemy.orm import relationship
from src.models.base import Base

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer(), primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    url = Column(String(250), nullable=False, unique=True)
    price = Column(Numeric(10, 2), nullable=False)
    description = Column(String(10000), nullable=False)
    image_url = Column(String(150), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))
    created_at = Column(DateTime(), default=func.current_timestamp())
    updated_at = Column(DateTime(), nullable=True)
    category = relationship("Category", back_populates="books")