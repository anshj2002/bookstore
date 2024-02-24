from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float
from app1.database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)
    genre = Column(String)
    price = Column(Float)
    quantity = Column(Integer)

class BookBase(BaseModel):
    title: str
    author: str
    genre: str
    price: float
    quantity: int
class BookCreate(BookBase):
    pass

class BookRES(BookBase):
    id: int

    class Config:
        orm_mode = True
