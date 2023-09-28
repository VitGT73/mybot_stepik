# op.create_table(
#     "step_types",
#     sa.Column("name", sa.String(length=10), nullable=False),
#     sa.Column("id", sa.Integer(), nullable=False),
#     sa.PrimaryKeyConstraint("id"),
#     sa.UniqueConstraint("name"),
# )

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class StepTypeBase(BaseModel):
    title: str
    course_id: int

    last_update: datetime | None = None


class StepTypeCreate(StepTypeBase):
    pass


class StepTypeUpdate(BaseModel):
    title: str | None = None
    course_id: int | None = None
    last_update: datetime | None = None


class StepTypeSchema(StepTypeBase):
    model_config = ConfigDict(from_attributes=True)

    id: int