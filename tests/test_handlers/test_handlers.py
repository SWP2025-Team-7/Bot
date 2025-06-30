import pytest

from unittest.mock import AsyncMock
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.base import StorageKey
from handlers import start_handler, restart_handler
from tests.utils import TEST_USER, TEST_USER_CHAT

from states import StudentStates
from texts import get_message
from enums import Messages

@pytest.mark.asyncio
async def test_start_handler(memory_storage, bot):
    message = AsyncMock()
    state = FSMContext(
        storage=memory_storage,
        key=StorageKey(
            bot_id=bot.id,
            user_id=TEST_USER.id,
            chat_id=TEST_USER_CHAT.id,
        )
    )
    await start_handler(msg=message, state=state)
    assert await state.get_state() is None
    
    message.delete.assert_any_call()

@pytest.mark.asyncio
async def test_restart_handler(memory_storage, bot):
    message = AsyncMock()
    state = FSMContext(
        storage=memory_storage,
        key=StorageKey(
            bot_id=bot.id,
            user_id=TEST_USER.id,
            chat_id=TEST_USER_CHAT.id,
        )
    )
    await restart_handler(msg=message, state=state)
    assert await state.get_state() is StudentStates.start
    message.answer.asser_called_with(get_message(message=Messages.INSTRUCTIONS, language=(await state.get_data()).get("language")))