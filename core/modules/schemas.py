# op.create_table(
#     "modules",
#     sa.Column("course_id", sa.Integer(), nullable=False),
#     sa.Column("id", sa.Integer(), nullable=False),
#     sa.Column("last_update", sa.DateTime(), nullable=True),
#     sa.Column("title", sa.String(length=60), nullable=False),
#     sa.ForeignKeyConstraint(
#         ["course_id"],
#         ["courses.id"],
#     ),
#     sa.PrimaryKeyConstraint("id"),
#     sa.UniqueConstraint("title"),
# )
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ModuleBase(BaseModel):
    title: str
    parent_id: int

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