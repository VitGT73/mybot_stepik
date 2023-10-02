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


class Courses:
    @classmethod
    async def create(cls, session: AsyncSession, course_create: CourseCreate) -> Course:
        course = Course(**course_create.model_dump())
        session.add(course)
        await session.commit()
        return course

    @classmethod
    async def get(cls, session: AsyncSession, course_id: int) -> Course | None:
        return await session.get(Course, course_id)

    @classmethod
    async def get_all(cls, session: AsyncSession) -> list[Course]:
        stmt = select(Course).order_by(Course.id)
        result: Result = await session.execute(statement=stmt)
        courses = result.scalars().all()
        return list(courses)

    @classmethod
    async def get_by_title(cls, session: AsyncSession, title: str) -> Course | None:
        stmt = select(Course).where(Course.title == title)
        course: Course | None = await session.scalar(statement=stmt)
        return course

    @classmethod
    async def update(cls, session: AsyncSession, course_id: int,
                     course_update: CourseUpdate) -> Course:
        course = await cls.get(session=session, course_id=course_id)
        for name, value in course_update.model_dump(exclude_unset=True).items():
            setattr(course, name, value)
        await session.commit()
        return course

    @classmethod
    async def delete(cls, session: AsyncSession, course_id: int) -> None:
        course = await session.get(Course, course_id)
        await session.delete(course)
        await session.commit()

    @classmethod
    async def delete_all(cls, session: AsyncSession) -> None:
        stmt = delete(Course)
        await session.execute(stmt)
        await session.commit()


async def add_courses(session: AsyncSession):
    start_courses = (
        ("Добрый, добрый Python - обучающий курс от Сергея Балакирева", "https://stepik.org/course/100707"),
        ("Поколение Python: курс для начинающих", "https://stepik.org/course/58852"),
        ("Поколение Python: курс для продвинутых", "https://stepik.org/course/68343"),
        ("Инди-курс программирования на Python", "https://stepik.org/course/63085"),
    )

    for course in start_courses:
        course_create = CourseCreate(
            title=course[0],
            url=course[1],
        )
        await Courses.create(session, course_create)


async def main():
    async with db_helper.session_factory() as session:
        await Courses.delete_all(session=session)
        await add_courses(session)

if __name__ == "__main__":
    asyncio.run(main())
