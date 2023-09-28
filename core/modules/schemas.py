from datetime import datetime

from pydantic import BaseModel, ConfigDict, HttpUrl


class ModuleBase(BaseModel):
    title: str
    url: str

    last_update: datetime | None = None


class ModuleCreate(ModuleBase):
    pass


class ModuleUpdate(BaseModel):
    title: str | None = None
    url: str | None = None
    last_update: datetime | None = None


class ModuleSchema:
    model_config = ConfigDict(from_attributes=True)

    id: int