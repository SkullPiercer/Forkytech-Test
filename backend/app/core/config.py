from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_title: str = "Тестовое задание"
    model_config = {"extra": "allow"}
    model_config = SettingsConfigDict(env_file=".env", extra="allow")


settings = Settings()
