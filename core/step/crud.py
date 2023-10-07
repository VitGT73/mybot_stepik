# op.create_table(
#     "steps",
#     sa.Column("number", sa.Integer(), nullable=False),
#     sa.Column("url", sa.String(length=2083), nullable=False),
#     sa.Column("image", sa.LargeBinary(), nullable=False),
#     sa.Column("lesson_id", sa.Integer(), nullable=False),
#     sa.Column("title", sa.String(length=60), nullable=False),
#     sa.Column("last_update", sa.DateTime(), nullable=True),
#     sa.Column("id", sa.Integer(), nullable=False),
#     sa.ForeignKeyConstraint(
#         ["lesson_id"],
#         ["lessons.id"],
#     ),
#     sa.PrimaryKeyConstraint("id"),
#     sa.UniqueConstraint("title"),
# )

import asyncio

from sqlalchemy import select, Result, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from core.models import Step, db_helper, BaseCRUD, Lesson, Module, Course
from core.step import StepSchema, StepCreate, StepUpdate


class Steps(BaseCRUD):
    ModelClass = Step
    CreateClass = StepCreate


    # @staticmethod
    # async def get_step_with_solution(session: AsyncSession) -> list[Step]:
    #     stmt = select(Step).options(joinedload(Step.solution)).order_by(Step.id)
    #     steps = await session.scalars(statement=stmt)
    #     return list(steps)


    @staticmethod
    async def delete_by_lesson_id(session: AsyncSession, lesson_id: int) -> None:
        stmt = delete(Step).where(Step.lesson_id == lesson_id)
        await session.execute(stmt)
        await session.commit()


    # @staticmethod
    # async def gen_image_name(sessinon: AsyncSession, step_id: int):
    #     stmt = select(Step).option(joinedload(Step.lesson)).where(Step.id == step_id)
    #     name = await sessinon.scalar(stmt)
    #     return name
async def main():
    async with db_helper.session_factory() as session:
        await Steps.delete_all(session=session)


if __name__ == "__main__":
    asyncio.run(main())
