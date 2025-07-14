import logging 

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot.bot_api import create_user, update_user
from bot.states import States
from bot.texts import get_message, get_button_text
from bot.enums import Languages, Messages

from bot.keyboards import get_main_keyboard

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message, state: FSMContext): 
    logging.info(f"User ID: {msg.from_user.id}, started the bot")
    # Reset state
    await state.clear()
    await state.set_state(States.start)
    await state.update_data(language=Languages.ENG)
    
    code, ans = create_user(user_id=msg.from_user.id, alias=msg.from_user.username)
    match code:
        case 200 | 201 | 400:
            await msg.answer(text=get_message(message=Messages.LOGIN_INSTRUCTIONS, language=(await state.get_data()).get("language")))
        case 422 | 500 | _:
            await msg.answer(text=get_message(message=Messages.ERROR, language=(await state.get_data()).get("language")))
            
@router.message(Command("login"), States.start)
async def login_handler(msg: Message, state: FSMContext):
    await state.set_state(States.default)
    code, ans = update_user(user_id=msg.from_user.id, fields={"mail": "e.kazakov@innopolis.university", 
                                                                "name:": "Egor", 
                                                                "surname": "Kazakov",
                                                                "patronomic": "Andreyevich",
                                                                "phone_number": "+7(999)999-99-99",
                                                                "citizens": "Russia",
                                                                "duty_to_work": "yes",
                                                                "duty_status": "working"})
    await msg.answer(text=get_message(message=Messages.LOGIN, language=(await state.get_data()).get("language")))
                    #  reply_markup=get_main_keyboard(language=(await state.get_data()).get("language")))
    