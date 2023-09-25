from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram import F
from bot.keyboards import CoursesCallbackFactory

router = Router()
router.callback_query.filter(F.data.startswith("courses"))


@router.callback_query(CoursesCallbackFactory.filter(F.action == "show_chapter"))
async def callbacks_show_chapter(
        callback: CallbackQuery,
        callback_data: CoursesCallbackFactory
):
    print(callback.data)

    # print(callback.model_dump_json(indent=4, exclude_none=True))
    await callback.answer(f"ID выбранного курса = {callback_data.value}")
    await callback.message.delete()

    # await state.update_data(gender=callback.data)
    # await callback.message.answer(text='Спасибо! А теперь загрузите, '
    #                                    'пожалуйста, ваше фото')
    # # Устанавливаем состояние ожидания загрузки фото
    # await state.set_state(FSMFillForm.upload_photo)



# Нажатие на кнопку "подтвердить"
@router.callback_query(CoursesCallbackFactory.filter(F.action == "cancel"))
async def callbacks_cancel(
        callback: CallbackQuery,
        callback_data: CoursesCallbackFactory
):
    # Текущее значение
    # user_value = user_data.get(callback.from_user.id, 0)
    #
    # user_data[callback.from_user.id] = user_value + callback_data.value
    # await callbacks_show_chapter(callback.message, user_value + callback_data.value)
    await callback.answer("Вы нажали 'cancel'")

