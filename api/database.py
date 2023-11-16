from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# TODO: turn me into an env var when done with local dev
SQLALCHEMY_DATABASE_URL = "postgresql://root:pass123@dmc-postgres:5432/dmc_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()