# https://youtu.be/KWu_RyTKh1s?t=2145
from datetime import datetime

from pydantic import BaseModel, ConfigDict, HttpUrl, field_serializer


class CursesBase(BaseModel):
    title: str
    url: str
    last_update: datetime | None = None


class CourseCreate(CursesBase):
    pass


class CourseUpdate(BaseModel):
    title: str | None = None
    url: HttpUrl
    last_update: datetime | None = None

    @field_serializer('url')
    def serialize_url(self, url: HttpUrl):
        return str(self.url)


class CourseSchema(CursesBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
