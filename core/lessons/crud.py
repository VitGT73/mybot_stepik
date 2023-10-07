# op.create_table(
#     "modules",
#     sa.Column("course_id", sa.Integer(), nullable=False),
#     sa.Column("title", sa.String(length=60), nullable=False),
#     sa.Column("last_update", sa.DateTime(), nullable=True),
#     sa.Column("id", sa.Integer(), nullable=False),
#     sa.ForeignKeyConstraint(
#         ["course_id"],
#         ["courses.id"],
#     ),
#     sa.PrimaryKeyConstraint("id"),
#     sa.UniqueConstraint("title"),
# )

import asyncio

from sqlalchemy import select, Result, ScalarResult, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload

# from core.lessons.schemas import LessonWithSteps
from core.models import Lesson, db_helper, BaseCRUD
from core.lessons import LessonCreate, LessonUpdate




class Lessons(BaseCRUD):
    ModelClass = Lesson
    CreateClass = LessonCreate

    @staticmethod
    async def get_with_steps(session: AsyncSession, lesson_id: int) -> ScalarResult:
        stmt = select(Lesson).options(selectinload(Lesson.step)).where(Lesson.id == lesson_id)
        result: Result = await session.execute(stmt)
        lesson: ScalarResult = result.scalars()
        return lesson

    @staticmethod
    async def get_by_module_id(session: AsyncSession, module_id: int) -> ScalarResult:
        stmt = select(Lesson).where(Lesson.module_id == module_id)
        items = await session.scalars(stmt)
        return items

    @staticmethod
    async def delete_by_module_id(session: AsyncSession, module_id: int) -> None:
        stmt = delete(Lesson).where(Lesson.module_id == module_id)
        await session.execute(stmt)
        await session.commit()


async def main():
    async with db_helper.session_factory() as session:
        await Lessons.get_all(session=session)





if __name__ == "__main__":
    asyncio.run(main())
