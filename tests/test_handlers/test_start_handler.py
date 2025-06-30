import pytest
from unittest.mock import AsyncMock

from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.base import StorageKey

from tests.utils import TEST_USER, TEST_USER_CHAT

from bot.states import StudentStates

from bot.handlers import start_handler

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
    assert await state.get_state() == StudentStates.start