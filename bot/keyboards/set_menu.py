from aiogram import Bot
from aiogram.types import BotCommand


async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command='/help',
                   description='Справка по работе бота'),
        BotCommand(command="/start",
                   description='Начало работы бота'),
        BotCommand(command='/support',
                   description='Поддержка'),
        BotCommand(command='/payments',
                   description='Платежи')]
    await bot.set_my_commands(main_menu_commands)
