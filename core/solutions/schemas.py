# op.create_table(
#     "solutions",
#     sa.Column("step_id", sa.Integer(), nullable=False),
#     sa.Column("image", sa.LargeBinary(), nullable=False),
#     sa.Column("code", sa.Text(), nullable=False),
#     sa.Column("id", sa.Integer(), nullable=False),
#     sa.Column("last_update", sa.DateTime(), nullable=True),
#     sa.ForeignKeyConstraint(
#         ["step_id"],
#         ["steps.id"],
#     ),
#     sa.PrimaryKeyConstraint("id"),
# )
from datetime import datetime

from pydantic import BaseModel, ConfigDict
# from sqlalchemy import LargeBinary


class SolutionBase(BaseModel):
    parent_id: int
    type: int | None = None
    code: str | None = None
    image: bytes | None = None
    last_update: datetime | None = None


class SolutionCreate(SolutionBase):
    pass


class SolutionUpdate(BaseModel):
    step_id: int
    type: int | None = None
    code: str | None = None
    image: bytes | None = None
    last_update: datetime | None = None


class SolutionSchema(SolutionBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


# class SolutionBase(BaseModel):
#     code: int = None
#     image: bytes = None
#     step_id: int
#     last_update: datetime = None
#
#
# class SolutionCreate(SolutionBase):
#     pass
#
#
# class SolutionUpdate(BaseModel):
#     code: int = None
#     image: bytes = None
#     step_id: int
#     last_update: datetime = None
#
#
# class SolutionSchema(SolutionBase):
#     id: int