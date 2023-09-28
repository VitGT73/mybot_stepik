from datetime import datetime

from pydantic import BaseModel, ConfigDict, HttpUrl, field_serializer
from sqlalchemy import LargeBinary


class StepBase(BaseModel):
    title: str | None = None
    number: int
    url: HttpUrl
    image: LargeBinary
    lesson_id: int
    last_update: datetime | None = None


class StepCreate(StepBase):
    pass


class StepUpdate(BaseModel):
    title: str | None = None
    number: int | None = None
    url: HttpUrl | None = None
    image: LargeBinary | None = None
    lesson_id: int | None = None
    last_update: datetime | None = None

    @field_serializer('url')
    def serialize_url(self, url: HttpUrl):
        return str(self.url)


class StepSchema(StepBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
