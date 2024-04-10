from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base
  
class Post(Base):
    __tablename__ = 'posts'
    id =  Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content= Column(String, nullable=True)
    published = Column(Boolean, nullable=True, default=True)
    rate = Column(Integer, nullable=True)
    post_date = Column(DateTime, default=datetime.now(), nullable=False)
    
class User(Base):
    __tablename__ = "users"
    id  = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, unique=True)
    hashed_password = Column(String, nullable=False)
    is_active  = Column(Boolean, default=True)
    #items = relationship("Item")

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String)
    description = Column(String)
    owner_id =  relationship(User, cascade = "all,delete", backref="id")
    
    