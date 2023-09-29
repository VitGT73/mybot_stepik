from datetime import datetime

from pydantic import BaseModel, ConfigDict, HttpUrl, field_serializer


class LessonBase(BaseModel):
    title: str
    url: str
    module_id: int
    last_update: datetime | None = None


class LessonCreate(LessonBase):
    pass


class LessonUpdate(BaseModel):
    title: str | None = None
    url: HttpUrl
    module_id: int
    last_update: datetime | None = None

    @field_serializer('url')
    def serialize_url(self, url: HttpUrl):
        return str(self.url)


class LessonSchema(LessonBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
