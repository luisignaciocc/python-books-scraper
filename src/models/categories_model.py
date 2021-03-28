from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.sql.elements import Null

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer(), primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    url = Column(String(100), nullable=False, unique=True)
    created_at = Column(DateTime(), default=func.current_timestamp())
    updated_at = Column(DateTime(), nullable=True)
    
    def __str__(self):
        return self.name

def migrate_table(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)