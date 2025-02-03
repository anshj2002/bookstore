from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

url = "postgresql://postgres:anshjain@localhost/fastapi"
engine = create_engine(url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.metadata.create_all(bind=engine)
def get_db(): 
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()