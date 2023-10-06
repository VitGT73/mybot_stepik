import asyncio

from sqlalchemy import select, Result, ScalarResult, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

# from core.lessons.schemas import LessonWithSteps
from core.models import Lesson, db_helper, BaseCRUD
from core.lessons import LessonCreate, LessonUpdate, Lessons

start_lessons = (
    ("1.1  Как правильно проходить этот курс", "https://www.mail.ru", 1),
    ("1.2  Первое знакомство с Python. Порядок установки", "https://www.mail.ru", 1),
    ("1.3  Варианты выполнения команд. Переходим в PyCharm", "https://www.mail.ru", 1),
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

lesson1 = (
    ("1.1  Как правильно проходить этот курс", "www.ya.ru", 1),
    ("1.2  Первое знакомство с Python. Порядок установки", "www.ya.ru", 1),
    ("1.3  Варианты выполнения команд. Переходим в PyCharm", "www.ya.ru", 1),
)
lesson2 = (
    ("2.1  Переменные, оператор присваивания, функции type и id", "https://www.mail.ru", 2),
    ("2.2  Числа и операции над ними", "https://www.mail.ru", 2),
    ("2.3  Математические функции и модуль math", "https://www.mail.ru", 2),
    ("2.4  Функции print и input", "https://www.mail.ru", 2),
    ("2.5  Логический тип Bool. Операторы сравнения", "https://www.mail.ru", 2),
)
lesson3 = (
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


async def add_lessons(session: AsyncSession):
    for lesson in start_lessons:
        lesson_create = LessonCreate(
            title=lesson[0],
            url=lesson[1],
            module_id=lesson[2],
        )
        await Lessons.create(session, lesson_create)



async def main():
    async with db_helper.session_factory() as session:
        await Lessons.delete_all(session=session)
        await add_lessons(session=session)



if __name__ == "__main__":
    asyncio.run(main())
