from typing import Optional

from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder

courses: dict = {
    'Инди-курс программирования на Python': 1,
    '"Поколение Python": курс для начинающих': 2,
    'Добрый, добрый Python': 3,
    '"Поколение Python": курс для продвинутых': 4
}
chapters: dict = {
    'Глава 1': 1,
    'Глава 2': 2,
    'Глава 3': 3,
    'Глава 4': 4,
    'Глава 5': 5,
    'Глава 6': 6,
    'Глава 7': 7
}

class CoursesCallbackFactory(CallbackData, prefix="courses"):
    action: str
    value: Optional[int] = None

class ChaptersCallbackFactory(CallbackData, prefix="chapter"):
    action: str
    value: Optional[int] = None


def get_keyboard_courses():
    builder = InlineKeyboardBuilder()
    # Наполняем клавиатуру кнопками-закладками в порядке возрастания
    for name, course_id in sorted(courses.items()):
        builder.button(
                text=f'{name}',
                callback_data=CoursesCallbackFactory(action="show_chapter", value=course_id)
            )
        # Добавляем в конец клавиатуры кнопку "Отменить"
    builder.button(
        text='Cancel',
        callback_data=CoursesCallbackFactory(action="cancel")
    )
    builder.adjust(1)
    return builder.as_markup()

def get_keyboard_chapters():
    builder = InlineKeyboardBuilder()
    # Наполняем клавиатуру кнопками-закладками в порядке возрастания
    for name, chapter_id in sorted(chapters.items()):
        builder.button(
                text=f'{name}',
                callback_data=ChaptersCallbackFactory(action="show_lesson", value=chapter_id)
            )
        # Добавляем в конец клавиатуры кнопку "Отменить"
    builder.button(
        text='Cancel',
        callback_data=ChaptersCallbackFactory(action="cancel")
    )
    builder.adjust(1)
    return builder.as_markup()