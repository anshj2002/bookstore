from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from app1.crud import create_book, get_all_books, get_book_by_title, update_book_by_title, delete_book_by_title, get_user_by_id, get_user_by_username, update_user, delete_user, create_user
from app1.models import Book, BookBase, BookCreate, BookRES, User, User1
from app1.database import engine, SessionLocal, Base
from fastapi import FastAPI, HTTPException
from passlib.context import CryptContext
pwd_context = CryptContext(schemes = ["bcrypt"] , deprecated = "auto")
Base.metadata.create_all(bind=engine)
app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users/", response_model=User)
def create_user(user: User, db: Session = Depends(get_db)):
    existing_user = get_user_by_username(db, user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed_password = pwd_context.hash(user.password)
    db_user = create_user(db, User1(username=user.username, password=hashed_password))
    return db_user

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: User, db: Session = Depends(get_db)):
    updated_user = update_user(db, user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@app.delete("/users/{user_id}", response_model=User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted_user = delete_user(db, user_id)
    if deleted_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted_user

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