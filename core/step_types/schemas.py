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
    name: str


class StepTypeCreate(StepTypeBase):
    pass


class StepTypeUpdate(BaseModel):
    name: str | None = None


class StepTypeSchema(StepTypeBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
