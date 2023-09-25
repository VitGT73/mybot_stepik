from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='src/.env', env_file_encoding='utf-8')
    bot_token: SecretStr
    # stepik_login: SecretStr
    # stepik_password: SecretStr
    #
    sql_url: str = "sqlite+aiosqlite:///db/db.sqlite3"
    sql_echo: bool = True


settings = Settings()
