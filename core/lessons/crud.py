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

from sqlalchemy import select, Result, ScalarResult, delete, and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload

# from core.lessons.schemas import LessonWithSteps
from core.models import Lesson, db_helper, BaseCRUD, Module, Course
from core.lessons import LessonCreate, LessonUpdate




class Lessons(BaseCRUD):
    ModelClass = Lesson
    CreateClass = LessonCreate

    @staticmethod
    async def get_with_steps(session: AsyncSession, lesson_id: int) -> ScalarResult:
        stmt = select(Lesson).options(selectinload(Lesson.step)).where(Lesson.id == lesson_id)
        result: Result = await session.execute(stmt)
        # хер знает что тут вернули в lesson, нужно проверить и создать вспомогательный класс в схемах
        lesson: ScalarResult = result.scalars()
        return lesson

    @staticmethod
    async def get_by_module_id(session: AsyncSession, module_id: int) -> row:
        stmt = select(Lesson).where(Lesson.module_id == module_id)
        items = await session.scalars(stmt)
        return items

    @staticmethod
    async def delete_by_module_id(session: AsyncSession, module_id: int) -> None:
        stmt = delete(Lesson).where(Lesson.module_id == module_id)
        await session.execute(stmt)
        await session.commit()


    # @staticmethod
    # async def get_stepik_id(session: AsyncSession, lesson_id: int) -> Lesson:
    #     stmt = select(Lesson.module_id).where(Lesson.id == lesson_id)
    #     print(stmt)
    #     module_id = await session.scalar(stmt)
    #     stmt = select(Course.stepik_id).join(Module).where(and_(Module.course_id == Course.id, Module.id==module_id))
    #     stepik_id = await session.scalar(stmt)
    #     return stepik_id

    @staticmethod
    async def get_stepik_id(session: AsyncSession, lesson_id: int) -> Lesson:
        stmt = select(Course.stepik_id).join(Course.module).join(Module.lesson).where(Lesson.id == lesson_id)
        stepik_id = await session.scalar(stmt)
        return stepik_id



async def main():
    async with db_helper.session_factory() as session:
        # await Lessons.get_all(session=session)
        stepik_id = await Lessons.get_stepik_id(session=session, lesson_id=1)
        print(stepik_id)




if __name__ == "__main__":
    asyncio.run(main())
