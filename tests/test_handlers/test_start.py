import pytest

from unittest.mock import AsyncMock
from aiogram.fsm.context import FSMContext
from aiogram.dispatcher.fsm.storage.base import StorageKey
from bot.handlers import start_handler
from tests.utils import TEST_USER, TEST_USER_CHAT

@pytest.mark.asyncio
async def test_start_handler(storage, bot):
    message = AsyncMock()
    state=FSMContext(
        bot=bot,
        storage=storage,
        key=StorageKey(
            bot_id=bot.id,
            user_id=TEST_USER.id,
            chat_id=TEST_USER_CHAT.id,
        )
    )
    await start_handler(msg=message, state=state)
    assert state.get_state() is None