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

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.courses import CourseUpdate, CourseCreate
from core.models import Course, db_helper


async def add_course(session: AsyncSession, course_create: CourseCreate) -> Course:
    course = Course(**course_create.model_dump())
    session.add(course)
    await session.commit()
    return course


async def get_courses(session: AsyncSession) -> list[Course]:
    stmt = select(Course).order_by(Course.id)
    result: Result = await session.execute(statement=stmt)
    courses = result.scalars().all()
    return list(courses)


async def get_course(session: AsyncSession, course_id: int) -> Course | None:
    return await session.get(Course, course_id)


async def update_course(
        session: AsyncSession,
        course: Course,
        course_update: CourseUpdate,
) -> Course:
    for name, value in course_update.model_dump(exclude_unset=True).items():
        print(name, value)
        setattr(course, name, value)
        print(course)
    await session.commit()
    return course


async def main():
    async with db_helper.session_factory() as session:
        upd_course = CourseUpdate(
            url="https://www.google.com/",
            title="Добрый, добрый Python - обучающий курс от Сергея Балакирева",
        )
        # lst = await get_courses(session=session)
        # print(lst)
        course = await get_course(session, 1)
        print(course)
        course = await update_course(session, course, upd_course)
        # print(course)
        # record = ("1.1 ВВедение",1)
        # await add_module(session=session, title=record[0],course_id= record[1])


if __name__ == "__main__":
    asyncio.run(main())
