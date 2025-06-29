import pytest

from unittest.mock import AsyncMock

from bot.handlers import start_handler

@pytest.mark.asyncio
async def test_start_handler():
    message = AsyncMock()
    await start_handler(message)

    message.answer.assert_called_with()