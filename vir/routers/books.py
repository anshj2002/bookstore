from fastapi import HTTPException, Depends, status
from typing import List
from sqlalchemy.orm import Session
from app1.crud import create_book, get_all_books, get_book_by_title, update_book_by_title, delete_book_by_title
from app1.models import BookCreate, BookRES, User
from app1.database import get_db
from app1.auth import get_current_user
from fastapi import HTTPException, APIRouter

router = APIRouter()

@router.post("/books/", response_model=BookRES, status_code=status.HTTP_202_ACCEPTED)
def create_new_book(book: BookCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_book(db=db, book=book)

@router.get("/books/", response_model=List[BookRES], status_code=status.HTTP_202_ACCEPTED)
def get_all_books_route(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_all_books(db=db)

@router.get("/books/{title}", response_model=BookRES, status_code=status.HTTP_202_ACCEPTED)
def get_book_by_title_route(title: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    book = get_book_by_title(db=db, title=title)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.put("/books/{title}", response_model=BookRES, status_code=status.HTTP_202_ACCEPTED)
def update_book_by_title_route(title: str, updated_book: BookCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    book = update_book_by_title(db=db, title=title, updated_book=updated_book)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.delete("/books/{title}", status_code=status.HTTP_202_ACCEPTED)
def delete_book_by_title_route(title: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)): #is_admin: bool = Depends(is_admin)):
    success = delete_book_by_title(db=db, title=title)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}