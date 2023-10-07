# op.create_table(
#     "courses",
#     sa.Column("url", sa.String(length=2083), nullable=False),
#     sa.Column("title", sa.String(length=60), nullable=False),
#     sa.Column("last_update", sa.DateTime(), nullable=True),
#     sa.Column("id", sa.Integer(), nullable=False),
#     sa.PrimaryKeyConstraint("id"),
#     sa.UniqueConstraint("title"),
# )
import asyncio

from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload

from core.courses import CourseCreate
from core.models import Course, db_helper, BaseCRUD, Module, Lesson


class Courses(BaseCRUD):
    ModelClass = Course
    CreateClass = CourseCreate

    @staticmethod
    async def get_by_title(session: AsyncSession, title: str) -> Course | None:
        stmt = select(Course).where(Course.title == title)
        item: Course | None = await session.scalar(statement=stmt)
        return item

    @staticmethod
    async def get_stepik_id_by_lesson_id(session: AsyncSession, lesson_id: int) -> int:
        stmt = select(Course.stepik_id).join(Course.modules).join(Module.lessons).where(Lesson.id == lesson_id)
        stepik_id = await session.scalar(stmt)
        return stepik_id


async def main():
    async with db_helper.session_factory() as session:
        stepik_id = await Courses.get_stepik_id_by_lesson_id(session=session, lesson_id=1)
        print(stepik_id)



if __name__ == "__main__":
    asyncio.run(main())
