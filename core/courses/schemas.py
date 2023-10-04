# https://youtu.be/KWu_RyTKh1s?t=2145

# op.create_table(
#     "courses",
#     sa.Column("url", sa.String(length=2083), nullable=False),
#     sa.Column("id", sa.Integer(), nullable=False),
#     sa.Column("last_update", sa.DateTime(), nullable=True),
#     sa.Column("title", sa.String(length=60), nullable=False),
#     sa.PrimaryKeyConstraint("id"),
#     sa.UniqueConstraint("title"),
# )
from datetime import datetime

from pydantic import BaseModel, ConfigDict, HttpUrl, field_serializer


class CursesBase(BaseModel):
    title: str
    stepik_id : int
    url: str
    last_update: datetime | None = None


class CourseCreate(CursesBase):
    pass


class CourseUpdate(BaseModel):
    title: str | None = None
    stepik_id: int | None = None
    url: HttpUrl
    last_update: datetime | None = None

    @field_serializer('url')
    def serialize_url(self, url: HttpUrl):
        return str(self.url)


class CourseSchema(CursesBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
