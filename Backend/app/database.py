import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
#connects python to postgre

SessionLocal = sessionmaker(
#lets API reqs talk to db
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
#used to create tables from python classes