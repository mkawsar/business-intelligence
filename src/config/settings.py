from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    DB_URL: str = os.getenv("DB_URL"),
    MONGO_INITDB_DATABASE: str = os.getenv("MONGO_INITDB_DATABASE"),
    JWT_PUBLIC_KEY: str = os.getenv("JWT_PUBLIC_KEY"),
    JWT_PRIVATE_KEY: str = os.getenv("JWT_PRIVATE_KEY"),
    REFRESH_TOKEN_EXPIRES_IN: int = os.getenv("REFRESH_TOKEN")
    ACCESS_TOKEN_EXPIRES_IN: int = os.getenv("ACCESS_TOKEN")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM")
    CLIENT_ORIGIN: str = os.getenv("CLIENT_ORIGIN")

settings = Settings()
