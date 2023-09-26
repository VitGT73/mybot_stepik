from pathlib import Path, PurePath,PureWindowsPath
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

BASE_DIR = Path(__file__).parent.parent.parent
DB_PATH = BASE_DIR / "core/db/db.sqlite3"
env_file = BASE_DIR  / ".env"

class Settings(BaseSettings):

    model_config = SettingsConfigDict(env_file=env_file, env_file_encoding='utf-8')
    bot_token: SecretStr
    stepik_login: SecretStr
    stepik_password: SecretStr
    #

    # sql_url: str = f"sqlite+aiosqlite://{SQLITEPATH}"
    sql_url: str = f"sqlite+aiosqlite:///{DB_PATH}"
    sql_echo: bool = True


settings = Settings()
