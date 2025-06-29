import os
import logging 
import asyncio

from aiogram import F, Router, exceptions
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message, ContentType
from aiogram.fsm.context import FSMContext

from bot import keyboards, states, enums
from bot.texts import get_message, get_button_text
from bot.enums import Languages, Messages, CallBacks

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message, state: FSMContext):
    logging.info(f"User ID: {msg.from_user.id}, started the bot")
    await state.clear()
    ans = bot_api.register_user(user_id=msg.from_user.id, alias=msg.from_user.username)
    if ans:
        await msg.answer(get_message(message=Messages.LANGUAGE, language=(await state.get_data()).get("language")),
                         reply_markup=keyboards.get_language_keyboard(language=(await state.get_data()).get("language")))
        await state.set_state(states.StudentStates.language)
    else:
        await msg.answer(get_message(message=Messages.ERROR))


@router.message(Command("language"))
async def language_handler(msg: Message, state: FSMContext):
    logging.info(f"User: {msg.from_user.id} changing language")
    await msg.answer(get_message(message=Messages.LANGUAGE, language=(await state.get_data()).get("language")),
                    reply_markup=keyboards.get_language_keyboard(language=(await state.get_data()).get("language")))
    await state.set_state(states.StudentStates.language)

@router.callback_query(states.StudentStates.language)
async def change_language(clbck:CallbackQuery, state: FSMContext):
    match clbck.data:
        case CallBacks.ru.value:
            logging.info(f"User: {clbck.from_user.id} changed language to {Languages.RU.value}")
            await state.update_data(language=Languages.RU)
        case CallBacks.eng.value:
            logging.info(f"User: {clbck.from_user.id} changed language to {Languages.ENG.value}")
            await state.update_data(language=Languages.ENG)
    await clbck.message.answer(text=get_message(message=Messages.LANGUAGE_CHANGED, language=(await state.get_data()).get("language")))
    await state.set_state(states.StudentStates.start)
    await clbck.message.answer(text=get_message(message=Messages.INSTRUCTIONS, language=(await state.get_data()).get("language")))


@router.message(Command("login"))
async def login_handler(msg: Message, state:FSMContext):
    await state.set_state(states.StudentStates.login)
    await msg.answer(text=get_message(message=Messages.LOGIN, language=(await state.get_data()).get("language")), 
                     reply_markup=keyboards.get_login_keyboard(language=(await state.get_data()).get("language")))
    await asyncio.sleep(4.0)
    await msg.answer(text="Successfully logged in!")
    await state.set_state(states.StudentStates.start)
    await msg.answer(text=get_message(message=Messages.INSTRUCTIONS, language=(await state.get_data()).get("language")))    

@router.message(Command("send"))
async def send_handler(msg: Message, state: FSMContext):
    logging.info(f"Waiting document from User ID: {msg.from_user.id}")
    await state.set_state(states.StudentStates.send)
    await msg.answer(text=get_message(message=Messages.SEND, language=(await state.get_data()).get("language")))

@router.message(states.StudentStates.send)
async def get_file(msg: Message, state: FSMContext):
    # match (msg.content_type):
    #     case ContentType.DOCUMENT:
    #         logging.info(f"Received the document from {msg.from_user.id}")
    #         file_id = msg.document.file_id
    #         file = await msg.bot.get_file(file_id)
    #         file_in_bytes = (await msg.bot.download_file(file.file_path)).read()
    #         ans = bot_api.send_document(user_id=msg.from_user.id, file_in_bytes=file_in_bytes)
    #         if ans:
    #             await msg.answer(enums.MessagesText.waiting_data_extraction.value)
    #         else:
    #             await msg.answer("Something is, wrong try later")
    #     case _:
    #         logging.info(f"Received the message instead of document from {msg.from_user.id}")
    await msg.answer("Извлечение данных...")
    await asyncio.sleep(4.0)
    await state.set_state(states.StudentStates.confirm)
    await msg.answer(text="Имя: Иван\nФамилия: Иванов\nОтчество: Иванович\n\nПозиция: Отличный работник\nКомпания: Хорошая работа\nЗП: 120.000₽\nДата начала работы: 2024-09-01",
                    reply_markup=keyboards.get_confirmation_keyboard(language=(await state.get_data()).get("language")))

@router.callback_query(states.StudentStates.confirm)
async def confirm_handler(clbck: CallbackQuery, state:FSMContext):
    await clbck.message.answer("Данный сохранены")

@router.message(Command("cancel"))
async def cancel_handler(msg: Message, state:FSMContext):
    logging.info(f"User: {msg.from_user.id}: canceled activity. Previous state: {(await state.get_state())}")
    await state.set_state(states.StudentStates.start)
    await msg.answer(text=get_message(message=Messages.CANCEL, language=(await state.get_data()).get("language")))
    await msg.answer(text=get_message(message=Messages.INSTRUCTIONS, language=(await state.get_data()).get("language")))

            