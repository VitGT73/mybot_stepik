from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ModuleBase(BaseModel):
    title: str
    course_id: int

    last_update: datetime | None = None


class ModuleCreate(ModuleBase):
    pass


class ModuleUpdate(BaseModel):
    title: str | None = None
    course_id: int | None = None
    last_update: datetime | None = None


class ModuleSchema(ModuleBase):
    model_config = ConfigDict(from_attributes=True)

    id: int