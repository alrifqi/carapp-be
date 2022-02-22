from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL = "mongodb://localhost:27017"
    UPLOAD_PATH = "assets/"


settings = Settings()
