# op.create_table(
#     "lessons",
#     sa.Column("url", sa.String(length=2083), nullable=False),
#     sa.Column("module_id", sa.Integer(), nullable=False),
#     sa.Column("id", sa.Integer(), nullable=False),
#     sa.Column("last_update", sa.DateTime(), nullable=True),
#     sa.Column("title", sa.String(length=60), nullable=False),
#     sa.ForeignKeyConstraint(
#         ["module_id"],
#         ["modules.id"],
#     ),
#     sa.PrimaryKeyConstraint("id"),
#     sa.UniqueConstraint("title"),
# )
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
