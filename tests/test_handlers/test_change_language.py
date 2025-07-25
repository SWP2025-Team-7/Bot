import pytest
from unittest.mock import AsyncMock

from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.base import StorageKey

from tests.utils import TEST_USER, TEST_USER_CHAT

from bot.states import StudentStates
from bot.enums import Messages
from bot.texts import get_message

from bot.handlers import change_language

@pytest.mark.asyncio
async def test_change_language(memory_storage, bot):
    call = AsyncMock()
    state = FSMContext(
        storage=memory_storage,
        key=StorageKey(
            bot_id=bot.id,
            user_id=TEST_USER.id,
            chat_id=TEST_USER_CHAT.id,
        )
    )
    await change_language(clbck=call, state=state)
    assert await state.get_state() == StudentStates.start
    call.message.answer.assert_called_with(text=get_message(message=Messages.LANGUAGE_CHANGED, language=(await state.get_data()).get("language")))