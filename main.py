import asyncio
import structlog
from bot.my_logging import SetupLogging
from core import config
from bot import start_bot

if __name__ == "__main__":
    logger = structlog.get_logger(__name__)
    logging_conf = SetupLogging()
    logging_conf.initStructlog()

    try:
        asyncio.run(start_bot(token=config.bot_token.get_secret_value()))
        # asyncio.run(start_bot(token='6344478735:AAFfpF53AKO6fYm8CFVh4JiDf9-KrQTRxW0'))
    except (KeyboardInterrupt, SystemError):
        print("-> Bot stopped!")
# config.bot_token.get_secret_value()