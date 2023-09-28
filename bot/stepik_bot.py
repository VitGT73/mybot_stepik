import asyncio
from aiogram import Bot, Dispatcher
from pydantic import SecretStr
# from my_logging import SetupLogging
# import structlog
from bot.handlers import handler_router
from bot.keyboards import set_main_menu
from core.config import settings


async def start_bot(token: str):
    # Инициализируем бот и диспетчер
    # bot = Bot(token=token)
    bot = Bot(token=token)

    dp = Dispatcher()

    # формируем меню бота
    dp.startup.register(set_main_menu)

    # Регистриуем роутеры в диспетчере
    dp.include_router(handler_router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    #  включаем логирование
    # logger = structlog.get_logger(__name__)
    # logging_conf = SetupLogging()
    # logging_conf.initStructlog()

    #  Запускаем бота
    asyncio.run(start_bot())
