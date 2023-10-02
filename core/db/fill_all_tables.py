import asyncio

from core.courses import CourseCreate, create_course
# from core.step_types import StepTypeCreate
# from core.step import StepCreate
#
# from core.lessons import LessonCreate
# from core.modules import ModuleCreate
# from core.solutions import SolutionCreate

from core.models import db_helper

start_courses = (
    ("Добрый, добрый Python - обучающий курс от Сергея Балакирева", "https://stepik.org/course/100707"),
    ("Поколение Python: курс для начинающих", "https://stepik.org/course/58852"),
    ("Поколение Python: курс для продвинутых", "https://stepik.org/course/68343"),
    ("Инди-курс программирования на Python", "https://stepik.org/course/63085"),
)

start_modules = (
    ("1  Первое знакомство", "www.gggfg.com"),
    ("2  Мои первые шаги в Python", "www.gggfg.com"),
    ("3  Постижение строк и списков", "www.gggfg.com"),
)

start_lessons = (
    ("1.1  Как правильно проходить этот курс", "www.ya.ru", 1),
    ("1.2  Первое знакомство с Python. Порядок установки", "www.ya.ru", 1),
    ("1.3  Варианты выполнения команд. Переходим в PyCharm", "www.ya.ru", 1),
    ("2.1  Переменные, оператор присваивания, функции type и id", "https://www.mail.ru", 2),
    ("2.2  Числа и операции над ними", "https://www.mail.ru", 2),
    ("2.3  Математические функции и модуль math", "https://www.mail.ru", 2),
    ("2.4  Функции print и input", "https://www.mail.ru", 2),
    ("2.5  Логический тип Bool. Операторы сравнения", "https://www.mail.ru", 2),
    ("3.1  Введение в строки. Операции над строками", "https://www.stepik.ru", 3),
    ("3.2  Индексы и срезы строк", "https://www.stepik.ru", 3),
    ("3.3  Основные методы строк", "https://www.stepik.ru", 3),
    ("3.4  Спецсимволы и экранирование символов", "https://www.stepik.ru", 3),
    ("3.5  Форматирование строк и F-строки", "https://www.stepik.ru", 3),
    ("3.6  Списки и операции над ними", "https://www.stepik.ru", 3),
    ("3.7  Срезы списков. Операторы сравнения списков", "https://www.stepik.ru", 3),
    ("3.8  Методы списков", "https://www.stepik.ru", 3),
    ("3.9  Вложенные списки", "https://www.stepik.ru", 3),
)

start_steps = (
    (1, "https://habr.com/", 1, 1),
    (2, "https://habr.com/", 1, 2),
    (3, "https://habr.com/", 1, 3),
    (4, "https://habr.com/", 1, 1),
    (1, "https://habr.com/", 2, 2),
    (2, "https://habr.com/", 2, 3),
    (3, "https://habr.com/", 2, 4),
    (4, "https://habr.com/", 2, 1),
    (5, "https://habr.com/", 2, 2),
    (1, "https://habr.com/", 3, 3),
    (2, "https://habr.com/", 3, 4),
    (3, "https://habr.com/", 3, 1),
    (4, "https://habr.com/", 3, 1),
    (5, "https://habr.com/", 3, 1),
)

start_step_type_names = ("review", "easy-quiz", "hard-quiz", "blank")


async def add_courses(courses: tuple):
    async with db_helper.session_factory() as session:
        for course in courses:
            course_create = CourseCreate(
                title=course[0],
                url=course[1],
            )
            await create_course(session, course_create)


async def main():
    await add_courses(start_courses)


if __name__ == "__main__":
    asyncio.run(main())
