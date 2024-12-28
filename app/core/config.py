import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_KEY: str = os.getenv("API_KEY")

    class Config:
        env_file = ".env"


def get_settings():
    return Settings()
