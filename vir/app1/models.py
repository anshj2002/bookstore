from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str
    genre: str
    price: float
    quantity: int

    class Config:
        orm_mode = True
