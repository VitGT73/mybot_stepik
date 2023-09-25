__all__ = ["handler_router"]

from .other_handlers import router as other_router, router_inline_missing
from .command_handlers import router as command_router
from .courses_handlers import router as courses_router
from aiogram import Router

# Инициализируем роутер уровня модуля
handler_router = Router()
# handler_router.message.filter()
handler_router.include_router(command_router)
handler_router.include_router(courses_router)
handler_router.include_router(router_inline_missing)
handler_router.include_router(other_router)

