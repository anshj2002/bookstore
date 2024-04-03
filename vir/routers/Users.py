from datetime import timedelta
from fastapi import FastAPI, HTTPException, Depends,APIRouter, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app1.crud import get_user_by_username, update_db_user, delete_user, create_db_user
from app1.models import User, User1
from app1.database import get_db
from app1.auth import authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from fastapi import FastAPI, HTTPException
from passlib.context import CryptContext
pwd_context = CryptContext(schemes = ["bcrypt"] , deprecated = "auto")
router = APIRouter()
@router.post("/users/", response_model=User)
def create_user(user: User, db: Session = Depends(get_db)):
    existing_user = get_user_by_username(db, user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    hashed_password = pwd_context.hash(user.password)
    
    db_user = create_db_user(db, User1(username=user.username, password=hashed_password))
    return user

@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: User, db: Session = Depends(get_db)):
    updated_user = update_db_user(db, user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/users/{user_id}", response_model=User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted_user = delete_user(db, user_id)
    if deleted_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted_user
@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user( form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
