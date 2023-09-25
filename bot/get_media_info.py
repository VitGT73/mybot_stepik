from aiogram import Bot, Dispatcher

# from aiogram.filters import CommandStart
#
# from aiogram.filters.callback_data import CallbackData
from core import config
from aiogram.types import (Message)

bot: Bot = Bot(token=config.bot_token.get_secret_value())

dp: Dispatcher = Dispatcher()


# Этот хэндлер будет срабатывать на команду /start

# и отправлять пользователю сообщение с клавиатурой

@dp.message()
async def process_start_command(message: Message):
    # print(message.json(indent=4, exclude_none=True))

    if "voice" in message.model_dump_json(indent=4, exclude_none=True):

        print("voice:")

        print(message.voice.file_id)

        print()

    elif "photo" in message.model_dump_json(indent=4, exclude_none=True):

        print("photo:")

        print(message.photo[0].file_id)

        print()



    elif "audio" in message.model_dump_json(indent=4, exclude_none=True):

        print("audio:")

        print(message.audio.file_id)

        print()



    elif "document" in message.model_dump_json(indent=4, exclude_none=True):

        print("document:")

        print(message.document.file_id)
        print(message.from_user)

        print()



    elif "video" in message.model_dump_json(indent=4, exclude_none=True):

        print("video:")

        print(message.video.file_id)

        print()


if __name__ == '__main__':
    dp.run_polling(bot)