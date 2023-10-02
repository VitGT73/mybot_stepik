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

from sqlalchemy import select, delete
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.courses import CourseUpdate, CourseCreate
from core.models import Course, db_helper


async def create_course(session: AsyncSession, course_create: CourseCreate) -> Course:
    course = Course(**course_create.model_dump())
    session.add(course)
    await session.commit()
    return course


async def get_course(session: AsyncSession, course_id: int) -> Course | None:
    return await session.get(Course, course_id)


async def get_all_courses(session: AsyncSession) -> list[Course]:
    stmt = select(Course).order_by(Course.id)
    result: Result = await session.execute(statement=stmt)
    courses = result.scalars().all()
    return list(courses)


async def get_course_by_title(session: AsyncSession, title: str) -> Course | None:
    stmt = select(Course).where(Course.title == title)
    course: Course | None = await session.scalar(statement=stmt)
    return course


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


async def delete_course(session: AsyncSession, course: Course) -> None:
    await session.delete(course)
    await session.commit()


async def delete_module_by_id(session: AsyncSession, module_id: int) -> None:
    course = await session.get(Course, module_id)
    await session.delete(course)
    await session.commit()


async def delete_all_courses(session: AsyncSession) -> None:
    stmt = delete(Course)
    await session.execute(stmt)
    await session.commit()


# start_courses = (
#     ("Добрый, добрый Python - обучающий курс от Сергея Балакирева", "https://stepik.org/course/100707"),
#     ("Поколение Python: курс для начинающих", "https://stepik.org/course/58852"),
#     ("Поколение Python: курс для продвинутых", "https://stepik.org/course/68343"),
#     ("Инди-курс программирования на Python", "https://stepik.org/course/63085"),
# )

async def add_courses(courses: tuple):
    async with db_helper.session_factory() as session:
        for course in courses:
            course_create = CourseCreate(
                title=course[0],
                url=course[1],
            )
            await create_course(session,course_create)


async def main():
    pass
    # await add_courses(start_courses)


    # async with db_helper.session_factory() as session:
    #     for course in start_courses:
    #         course_create = CourseCreate(
    #             title=course[0],
    #             url=course[1],
    #         )
    #         await create_course(session,course_create)

if __name__ == "__main__":
    asyncio.run(main())
