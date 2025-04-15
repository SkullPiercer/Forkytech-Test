from pydantic_settings import BaseSettings
from pydantic import Extra


class Settings(BaseSettings):
    app_title: str = "Бронирование переговорок"

    class Config:
        env_file = ".env"
        extra = Extra.allow


settings = Settings()
