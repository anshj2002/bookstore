from fastapi import FastAPI, HTTPException
from typing import List
from app1.crud import create_book, get_all_books, get_book_by_title, update_book_by_title, delete_book_by_title
from app1.models import Book

app = FastAPI()

@app.post("/books/", response_model=Book)
def create_new_book(book: Book):
    return create_book(book)

@app.get("/books/", response_model=List[Book])
def get_all_books_route():
    return get_all_books()

@app.get("/books/{title}", response_model=Book)
def get_book_by_title_route(title: str):
    book = get_book_by_title(title)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.put("/books/{title}", response_model=Book)
def update_book_by_title_route(title: str, updated_book: Book):
    book = update_book_by_title(title, updated_book)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.delete("/books/{title}")
def delete_book_by_title_route(title: str):
    success = delete_book_by_title(title)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}