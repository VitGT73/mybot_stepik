from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.utils.formatting import t

from bot.keyboards import CoursesCallbackFactory

# Инициализируем роутер уровня модуля
router = Router()
router_inline_missing = Router()


@router.message(F.text == "html")
async def send_echo(message: Message):
    user_id = message.from_user.id
    await bot.send_chat_action(user_id, ChatActions.UPLOAD_DOCUMENT)
    await asyncio.sleep(1)  # скачиваем файл и отправляем его пользователю
    await bot.send_document(user_id, TEXT_FILE,
                            caption='Этот файл специально для тебя!')

#     msg = bold(text("fwwfwefwe","wefwefwe"))
#     txt = '''
#
# Если, вдруг, вы почему-то решили удалить из проекта виртуальное окружение, сделать это можно просто удалив папку <code>venv</code> (или с другим названием, если вы, при создании виртуального окружения, называли ее по-другому).
#
#     '''
#     try:
#         await message.reply(text=text, parse_mode='HTML')
#         # await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         await message.reply(text='Моя - твоя не понимает! Набери /help если не знаешь что делать!')


@router.message()
async def send_echo(message: Message):
    try:
        await message.reply(text='Моя - твоя не понимает! Набери /help если не знаешь что делать!')
        # await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text='Моя - твоя не понимает! Набери /help если не знаешь что делать!')


@router.callback_query(CoursesCallbackFactory.filter())
async def callbacks_missing_handler(
        callback: CallbackQuery,
        callback_data: CoursesCallbackFactory
):
    print(f"Нажата inline кнопка из callbacks_missing_handler: {callback.data}")
    print(callback_data)
    await callback.answer()
