from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr, BaseModel

BASE_DIR = Path(__file__).parent.parent.parent
DB_PATH = BASE_DIR / "core/db/db.sqlite3"
env_file = BASE_DIR / ".env"



class DbSettings(BaseSettings):
    url: str = f"sqlite+aiosqlite:///{DB_PATH}"
    echo: bool = True


class BotSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=env_file,
        env_file_encoding='utf-8',
        extra="ignore",
        env_prefix="BOT_"
    )
    token: str
    pass

class StepikSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=env_file,
        env_file_encoding='utf-8',
        extra="ignore",
        env_prefix="STEPIK_"
    )
    login: str
    password: str


class Settings(BaseSettings):

    model_config = SettingsConfigDict(env_file=env_file, env_file_encoding='utf-8',extra="ignore")


    db: DbSettings = DbSettings()
    bot: BotSettings = BotSettings()
    stepik: StepikSettings = StepikSettings()

    #


settings = Settings()
print(settings)