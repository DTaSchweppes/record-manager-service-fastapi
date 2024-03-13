import os
from functools import lru_cache
from dotenv import load_dotenv
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()

print(os.getenv("SQL_URL"))


class Settings(BaseSettings):
    #model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    API_V1_STR: str = '/api/v1'
    TITLE: str = 'Record Manager'
    VERSION: str = '0.0.1'
    ASYNCPG_URL: PostgresDsn = os.getenv("SQL_URL")
    #asyncpg_url: str = os.getenv("SQL_URL")
    DESCRIPTION: str = 'Record Manager service'
    DOCS_URL: str | None = f'{API_V1_STR}/docs'
    REDOCS_URL: str | None = f'{API_V1_STR}/redocs'
    OPENAPI_URL: str | None = f'{API_V1_STR}/openapi'


@lru_cache
def get_settings():
    '''
    @lru_cache - кеширует результаты функции. Кеш хранится во внутренней структуре данных
    Возвращает класс Settings - с настройками
    :return:
    '''
    return Settings()


settings = get_settings()
