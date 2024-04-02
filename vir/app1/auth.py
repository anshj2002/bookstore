from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from  .database import get_db
from flask import session
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from typing import Any, List, Dict, Optional, Union
SECRET_KEY = "09d25e094faa6ca25hgkjhgkjjkkhhj3b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# Function to create access token
def create_access_token(data: Dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
def authenticate_user( username: str, password: str, db: Session = Depends(get_db)) -> Union[bool, Any]:
    from app1.crud import get_user_by_username
    user = get_user_by_username(db, username)
    if not user or not verify_password(password, user.password):
        return False
    return user

# Function to decode access token
def decode_access_token(token: str) -> Union[str, Dict[str, Any]]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
def verify_token(token: str, credentials_exception,  db: Session = Depends(get_db) ):
    from app1.crud import get_user_by_username
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        user = get_user_by_username( db, username)
        if user is None:
            return None
        return user
    except jwt.JWTError:
        return None
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user = verify_token(token, credentials_exception, db)
    if user is None:
        raise credentials_exception
    return user