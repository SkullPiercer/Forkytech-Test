from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Settings:
    email = getenv("EMAIL")
    api_v2_key = getenv("API_V2_KEY")
    branch = getenv("BRANCH")
    database_url = getenv("DATABASE_URL")


settings = Settings()
