from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from app1.crud import create_book, get_all_books, get_book_by_title, update_book_by_title, delete_book_by_title
from app1.models import Book, BookBase, BookCreate, BookRES
from app1.database import engine, SessionLocal, Base
Base.metadata.create_all(bind=engine)
app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/books/", response_model=BookRES)
def create_new_book(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db=db, book=book)

@app.get("/books/", response_model=List[BookRES])
def get_all_books_route(db: Session = Depends(get_db)):
    return get_all_books(db=db)

@app.get("/books/{title}", response_model=BookRES)
def get_book_by_title_route(title: str, db: Session = Depends(get_db)):
    book = get_book_by_title(db=db, title=title)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.put("/books/{title}", response_model=BookRES)
def update_book_by_title_route(title: str, updated_book: BookCreate, db: Session = Depends(get_db)):
    book = update_book_by_title(db=db, title=title, updated_book=updated_book)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.delete("/books/{title}")
def delete_book_by_title_route(title: str, db: Session = Depends(get_db)):
    success = delete_book_by_title(db=db, title=title)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}