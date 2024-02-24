from typing import List
from app1.database import SessionLocal
from sqlalchemy.orm import Session

from .models import Book, BookCreate


def create_book(book: BookCreate, db: Session):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_all_books(db: Session):
    return db.query(Book).all()

def get_book_by_title(title: str,db: Session):
    return db.query(Book).filter(Book.title == title).first()

def update_book_by_title(title: str, updated_book: BookCreate, db: Session):
    book = db.query(Book).filter(Book.title == title).first()
    if book:
        for attr, value in updated_book.dict().items():
            setattr(book, attr, value) if value else None
        db.commit()
        db.refresh(book)
        return book
    return None


def delete_book_by_title(title: str, db: Session):
    book = db.query(Book).filter(Book.title == title).first()
    if book:
        db.delete(book)
        db.commit()
        return True
    return False
