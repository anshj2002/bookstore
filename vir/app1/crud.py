from typing import List

from .models import Book

books_db = []

def create_book(book: Book):
    books_db.append(book)
    return book

def get_all_books():
    return books_db

def get_book_by_title(title: str):
    for book in books_db:
        if book.title == title:
            return book
    return None

def update_book_by_title(title: str, updated_book: Book):
    for i, book in enumerate(books_db):
        if book.title == title:
            books_db[i] = updated_book
            return updated_book
    return None

def delete_book_by_title(title: str):
    for i, book in enumerate(books_db):
        if book.title == title:
            del books_db[i]
            return True
    return False
