from typing import List, Optional
from sqlalchemy.orm import Session
from .models import User, User1
from .models import Book, BookCreate
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
    return db.query(User1).filter(User1.id == user_id).first()

# Function to get a user by username
def get_user_by_username(db: Session, username: str) -> Optional[User]:
    return db.query(User1).filter(User1.username == username).first()

# Function to create a new user
def create_db_user(db: Session, user: User1) -> Optional[User1]:
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
# Function to update user details
def update_db_user(db: Session, user_id: int, user: User) -> Optional[User]:
    db_user = db.query(User1).filter(User1.id == user_id).first()
    if db_user:
        db_user.username = user.username
        db_user.password = user.password
        db.commit()
        db.refresh(db_user)
        return db_user
    return None

# Function to delete a user
def delete_user(db: Session, user_id: int) -> Optional[User]:
    db_user = db.query(User1).filter(User1.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user
    return None

def create_book(book: BookCreate, db: Session):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_all_books(db: Session) -> List[Book]:
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