"""Configurations for ENV vars"""

from decouple import config

# TODO if this doesnt mesh switch to import os and os.getenv

class Config:
    DB_USER = config("DB_USER", "postgres")
    DB_PASSWORD = config("DB_PASSWORD", "postgres")
    DB_HOST = config("DB_HOST", "localhost:5555")
    DB_NAME = config("DB_NAME", "postgres")
    DB_CONFIG = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    BCRYPT_LOG_ROUNDS = 13


configuration = Config