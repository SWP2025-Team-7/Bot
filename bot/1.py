import os
import logging 
import asyncio

from aiogram import F, Router, exceptions
from aiogram.filters import Command, or_f
from aiogram.types import CallbackQuery, Message, ContentType
from aiogram.fsm.context import FSMContext

from bot import keyboards, states, enums, bot_api
from bot.states import States
from bot.texts import get_message, get_button_text, get_data_message
from bot.enums import Languages, Messages, CallBacks
            
# @router.message(Command("login"))
            
# @router.message(Command("cancel"))
# async def cancel_handler(msg: Message, state:FSMContext):
#     logging.info(f"User: {msg.from_user.id}: canceled activity. Previous state: {(await state.get_state())}")
#     await state.set_state(states.StudentStates.start)
#     await msg.answer(text=get_message(message=Messages.CANCEL, language=(await state.get_data()).get("language")))
#     await msg.answer(text=get_message(message=Messages.INSTRUCTIONS, language=(await state.get_data()).get("language")))

# @router.message(Command("restart"))
# async def restart_handler(msg: Message, state: FSMContext):
#     await state.clear()
#     await state.set_state(states.StudentStates.start)
#     await msg.answer(text=get_message(message=Messages.INSTRUCTIONS, language=(await state.get_data()).get("language")))


# @router.message(Command("login"), states.StudentStates.start)
# async def login_handler(msg: Message, state:FSMContext):
#     logging.info(f"Waiting authorization from user: {msg.from_user.id}")
#     # await state.set_state(states.StudentStates.login)
#     await msg.answer(text="Login with SSO is not awailable now")
#     # await msg.answer(text=get_message(message=Messages.LOGIN, language=(await state.get_data()).get("language")), 
#     #                  reply_markup=keyboards.get_login_keyboard(language=(await state.get_data()).get("language")))
#     # await asyncio.sleep(4.0)
#     # await msg.answer(text="Successfully logged in!")
#     # await state.set_state(states.StudentStates.start)
#     # await msg.answer(text=get_message(message=Messages.INSTRUCTIONS, language=(await state.get_data()).get("language")))    

# @router.message(Command("send"), states.StudentStates.start)
# async def send_handler(msg: Message, state: FSMContext):
#     logging.info(f"Waiting document from User ID: {msg.from_user.id}")
#     await state.set_state(states.StudentStates.send)
#     await msg.answer(text=get_message(message=Messages.SEND, language=(await state.get_data()).get("language")))

# @router.message(states.StudentStates.send)
# async def get_file(msg: Message, state: FSMContext):
#     match (msg.content_type):
#         case ContentType.DOCUMENT:
#             logging.info(f"Received the document from {msg.from_user.id}")
#             file_id = msg.document.file_id
#             file = await msg.bot.get_file(file_id)
#             status_code, data_json = bot_api.send_document(user_id=msg.from_user.id, file_path=file.file_path)
#             if status_code == 200:
#                 await msg.answer(text=get_data_message(data=data_json['output'], language=(await state.get_data()).get("language")))
#             else:
#                 await state.set_state(states.StudentStates.start)
#                 await msg.answer(text=get_message(message=Messages.ERROR, language=(await state.get_data()).get("language")))
#         case _:
#             logging.info(f"Received the message instead of document from {msg.from_user.id}")

# # @router.callback_query(states.StudentStates.confirm)
# # async def confirm_handler(clbck: CallbackQuery, state:FSMContext):
    

            