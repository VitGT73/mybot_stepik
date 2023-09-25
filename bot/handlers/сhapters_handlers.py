from aiogram import Router
from aiogram.types import CallbackQuery

from bot.keyboards import CoursesCallbackFactory

# Инициализируем роутер уровня модуля
router = Router()
router.message.filter()


@router.callback_query()
async def choice_chapter(callback: CallbackQuery,
                         callback_data: CoursesCallbackFactory):
    await callback.message.answer(
        text=f'Категория товаров: {callback_data.category_id}\n' \
             f'Подкатегория товаров: {callback_data.subcategory_id}\n' \
             f'Товар: {callback_data.item_id}')
    await callback.answer()
