from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

class Form(StatesGroup):
    course = State()
    chapter = State()
    lesson = State()