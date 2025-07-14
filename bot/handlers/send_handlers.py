import logging 

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType, CallbackQuery
from aiogram.fsm.context import FSMContext

from bot.bot_api import send_document, update_user
from bot.states import States
from bot.texts import get_message, get_button_text, get_data_message
from bot.enums import Languages, Messages
from bot.keyboards import get_confirmation_keyboard

router = Router()

@router.message(Command("send"), States.default)
async def send_handler(msg: Message, state: FSMContext):
    logging.info(f"Waiting document from User ID: {msg.from_user.id}")
    await state.set_state(States.send)
    await msg.answer(text=get_message(message=Messages.SEND, language=(await state.get_data()).get("language")))

@router.message(States.send)
async def get_file(msg: Message, state: FSMContext):
    match (msg.content_type):
        case ContentType.DOCUMENT:
            logging.info(f"Received the document from {msg.from_user.id}")
            file_id = msg.document.file_id
            file = await msg.bot.get_file(file_id)
            status_code, data_json = send_document(user_id=msg.from_user.id, file_path=file.file_path)
            
            
            if status_code == 200:
                await msg.answer(text=get_data_message(data=data_json['output'], language=(await state.get_data()).get("language")),
                                 reply_markup=get_confirmation_keyboard(language=(await state.get_data()).get("language")))
                data = {
                    'company': data_json['output']['company'],
                    'position': data_json['output']['position'],
                    'salary': data_json['output']['salary'],
                    'start_date': data_json['output']['startDate'],
                }
                
                await state.update_data(send=data)
            else:
                await state.set_state(States.start)
                await msg.answer(text=get_message(message=Messages.ERROR, language=(await state.get_data()).get("language")))
        case _:
            logging.info(f"Received the message instead of document from {msg.from_user.id}")
            await msg.answer(text=get_message(message=Messages.ERROR, language=(await state.get_data()).get("language")))
            
@router.callback_query(States.send, F.data == "confirm")
async def confirm_handler(clbck: CallbackQuery, state: FSMContext):
    logging.info(f"User {clbck.from_user.id} confirmed the extracted data")
    code, ans = update_user(user_id=clbck.from_user.id, fields=(await state.get_data()).get("send"))
    await state.set_state(States.start)
    await clbck.message.answer(text=get_message(message=Messages.THANKS, language=(await state.get_data()).get("language")))