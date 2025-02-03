from fastapi import FastAPI
from passlib.context import CryptContext
from routers import Users, books
pwd_context = CryptContext(schemes = ["bcrypt"] , deprecated = "auto")
app = FastAPI()

app.include_router(Users.router)
app.include_router(books.router)