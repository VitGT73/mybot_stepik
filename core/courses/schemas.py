# https://youtu.be/KWu_RyTKh1s?t=2145
from datetime import datetime

from pydantic import BaseModel, ConfigDict, HttpUrl




class CursesBase(BaseModel):
    title: str
    url: HttpUrl

    last_update: datetime | None = None


class CourseCreate(BaseModel):
    pass


class CourseUpdate(BaseModel):
    title: str | None = None
    url: str | None = None
    last_update: datetime | None = None


class CourseSchema:
    model_config = ConfigDict(from_attributes=True)

    id: int

