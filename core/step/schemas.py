# op.create_table(
#     "steps",
#     sa.Column("number", sa.Integer(), nullable=False),
#     sa.Column("url", sa.String(length=2083), nullable=False),
#     sa.Column("image", sa.LargeBinary(), nullable=False),
#     sa.Column("lesson_id", sa.Integer(), nullable=False),
#     sa.Column("step_type_id", sa.Integer(), nullable=False),
#     sa.Column("id", sa.Integer(), nullable=False),
#     sa.Column("last_update", sa.DateTime(), nullable=True),
#     sa.ForeignKeyConstraint(
#         ["lesson_id"],
#         ["lessons.id"],
#     ),
#     sa.ForeignKeyConstraint(
#         ["step_type_id"],
#         ["step_types.id"],
#     ),
#     sa.PrimaryKeyConstraint("id"),
# )

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
