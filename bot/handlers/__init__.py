from aiogram import Router

from .start_handlers import router as start_handlers_router
from .send_handlers import router as send_handlers_router
from .language_handlers import router as language_handlers_router

router = Router()

router.include_routers(
    start_handlers_router, 
    send_handlers_router,
    language_handlers_router
    )