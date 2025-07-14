import logging 

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ContentType, CallbackQuery
from aiogram.fsm.context import FSMContext

from bot.bot_api import send_document
from bot.states import States
from bot.texts import get_message, get_button_text, get_data_message
from bot.enums import Languages, Messages, CallBacks
from bot.keyboards import get_language_keyboard

router = Router()

@router.message(Command("language"), States.start)
async def language_handler(msg: Message, state: FSMContext):
    logging.info(f"User: {msg.from_user.id} changing language")
    await msg.answer(text=get_message(message=Messages.LANGUAGE, language=(await state.get_data()).get("language")),
                    reply_markup=get_language_keyboard(language=(await state.get_data()).get("language")))
    await state.set_state(States.language)

@router.callback_query(States.language)
async def change_language(clbck: CallbackQuery, state: FSMContext):
    match clbck.data:
        case CallBacks.ru.value:
            logging.info(f"User: {clbck.from_user.id} changed language to {Languages.RU.value}")
            await state.update_data(language=Languages.RU)
        case CallBacks.eng.value:
            logging.info(f"User: {clbck.from_user.id} changed language to {Languages.ENG.value}")
            await state.update_data(language=Languages.ENG)
    await clbck.message.answer(text=get_message(message=Messages.LANGUAGE_CHANGED, language=(await state.get_data()).get("language")))
    await state.set_state(States.start)