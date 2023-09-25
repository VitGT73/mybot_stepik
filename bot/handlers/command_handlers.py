from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from bot.keyboards import get_keyboard_courses

# Инициализируем роутер уровня модуля
router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Это инлайн-кнопки с параметром "url"',
                         reply_markup=get_keyboard_courses())


#

# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    text = 'Вы можете использовать следующие команды: \n' \
           '/help - Вы увидите эту подсказку\n' \
           '/start - запустить бота \n' \
           'или наберите /help <command>, \n' \
           'чтобы получить помощь по нужной команде'
    await message.answer(text=text)


# Этот хэндлер срабатывает на команду /Support
@router.message(Command(commands='support'))
async def process_support_command(message: Message):
    text = 'Бот находиться в режиме разработки! \n' \
           'Напишите ваш вопрос в чате бота \n' \
           'и постараюсь вам ответить \n' \
           ' (пока не реализовано)\n'
    await message.answer(text=text)


# Этот хэндлер срабатывает на команду /Support
@router.message(Command(commands='payments'))
async def process_payments_command(message: Message):
    text = 'Бот находиться в режиме разработки, \n' \
           'поэтому все функции пока бесплатные!'
    await message.answer(text=text)


@router.message(Command(commands='my_info'))
async def process_my_info_command(message: Message):
    await message.answer(text=f'Ваш ID: {message.from_user.id}')
    await message.answer(text=f'Ваше имя: {message.from_user.first_name}')
