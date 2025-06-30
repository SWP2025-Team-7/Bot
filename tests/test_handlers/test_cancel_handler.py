import pytest
from unittest.mock import AsyncMock
import datetime

from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.base import StorageKey

from tests.utils import TEST_USER, TEST_USER_CHAT

from bot.states import StudentStates
from bot.enums import Messages
from bot.texts import get_message

from bot.handlers import cancel_handler

@pytest.mark.asyncio
async def test_cancel_handler(memory_storage, bot):
    message = Message(
        message_id=42,
        date=datetime.datetime.now(),
        text="/cancel",
        chat=TEST_USER_CHAT,
        from_user=TEST_USER
    )
    state = FSMContext(
        storage=memory_storage,
        key=StorageKey(
            bot_id=bot.id,
            user_id=TEST_USER.id,
            chat_id=TEST_USER_CHAT.id,
        )
    )
    await cancel_handler(msg=message, state=state)
    assert await state.get_state() == StudentStates.start
    # message.answer.assert_called_with(get_message(message=Messages.CANCEL, language=(await state.get_data()).get("language")))
    message.answer.assert_called_with(get_message(message=Messages.INSTRUCTIONS, language=(await state.get_data()).get("language")))
