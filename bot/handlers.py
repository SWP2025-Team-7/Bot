import os
import logging 
import asyncio

from aiogram import F, Router, exceptions
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message, ContentType
from aiogram.fsm.context import FSMContext

import keyboards
import enums
import bot_api
import states

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message, state: FSMContext):
    logging.info(f"User ID: {msg.from_user.id}, started the bot")
    await state.set_state(states.StudentStates.start)
    ans = bot_api.register_user(user_id=msg.from_user.id, alias=msg.from_user.username)
    if ans:
        await msg.answer(enums.MessagesText.start_message.value)
    else:
        await msg.answer(enums.MessagesText.error_message.value)

@router.message(Command("send"))
async def send_handler(msg: Message, state: FSMContext):
    logging.info(f"Waiting document from User ID: {msg.from_user.id}")
    await state.set_state(states.StudentStates.send)
    await msg.answer(enums.MessagesText.send_instructions.value)

@router.message(states.StudentStates.send)
async def get_file(msg: Message, state: FSMContext):
    match (msg.content_type):
        case ContentType.DOCUMENT:
            logging.info(f"Received the document from {msg.from_user.id}")
            file_id = msg.document.file_id
            file = await msg.bot.get_file(file_id)
            file_in_bytes = (await msg.bot.download_file(file.file_path)).read()
            ans = bot_api.send_document(user_id=msg.from_user.id, file_in_bytes=file_in_bytes)
            if ans:
                await msg.answer(enums.MessagesText.waiting_data_extraction.value)
            else:
                await msg.answer("Something is,wrong try later")
        case _:
            logging.info(f"Received the message instead of document from {msg.from_user.id}")
            