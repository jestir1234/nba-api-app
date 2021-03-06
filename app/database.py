from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL: str = 'mysql+pymysql://{0}:{1}@{2}:3308/{3}'.format(  # noqa: E501
        os.environ.get('DB_USERNAME', ''),
        os.environ.get('DB_PASSWORD', ''),
        os.environ.get('DB_HOST', ''),
        os.environ.get('DB_SCHEMA', '')
    ) 

Engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    pool_pre_ping=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)

Base = declarative_base()

def get_session():
    try:
        session = SessionLocal()
        yield session
    finally:
        session.close()
