from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# TODO: turn me into an env var when done with local dev
# TODO: shift to sqlite to start to unblock dev time 
SQLALCHEMY_DATABASE_URL = "sqlite:///./dm_codex.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://root:pass123@dmc-postgres:5432/dmc_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}) # NOTE: needed for SQLite
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
