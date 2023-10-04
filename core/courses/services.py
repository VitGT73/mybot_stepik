import asyncio

from sqlalchemy.ext.asyncio import AsyncSession
from core.courses import CourseUpdate, CourseCreate
from core.models import db_helper
from core.courses import Courses



async def add_courses(session: AsyncSession):
    start_courses = (
        ("Добрый, добрый Python - обучающий курс от Сергея Балакирева", "https://stepik.org/course/100707", 100707),
        ("Поколение Python: курс для начинающих", "https://stepik.org/course/58852", 58852),
        ("Поколение Python: курс для продвинутых", "https://stepik.org/course/68343", 68343),
        ("Инди-курс программирования на Python", "https://stepik.org/course/63085", 63085),
    )

    for course in start_courses:
        course_create = CourseCreate(
            title=course[0],
            url=course[1],
            stepik_id=course[2]
        )
        await Courses.create(session, course_create)


async def main():
    async with db_helper.session_factory() as session:
        await Courses.delete_all(session=session)
        await add_courses(session)
        course = await Courses.get_by_title(session=session, title="Инди-курс программирования на Python")
        print(course.title)


if __name__ == "__main__":
    asyncio.run(main())