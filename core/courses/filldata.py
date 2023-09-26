import asyncio

from core.courses.crud import add_course
from core.models import db_helper

list_courses = [
    ("Добрый, добрый Python - обучающий курс от Сергея Балакирева",
     "https://stepik.org/course/100707"),
    ("Поколение Python: курс для начинающих",
     "https://stepik.org/course/58852"),
    ("Поколение Python: курс для продвинутых",
     "https://stepik.org/course/68343"),
    ("Инди-курс программирования на Python",
     "https://stepik.org/course/63085"),
]


async def fill_courses(courses: list[(str, str)]):
    async with db_helper.session_factory() as session:
        for title, url in courses:
            await add_course(session=session, title=title, url=url)


if __name__ == "__main__":
    asyncio.run(fill_courses(list_courses))
