from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer(), primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    url = Column(String(100), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.now())
    updated_at = Column(DateTime(), default=datetime.now())
    
    def __str__(self):
        return self.name

def migrate_table(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)