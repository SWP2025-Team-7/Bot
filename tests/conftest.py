import asyncio
import sys
from pathlib import Path

import pytest
import pytest_asyncio
from _pytest.config import UsageError

from aiogram import Dispatcher
from aiogram.fsm.storage.base import StorageKey
from aiogram.fsm.storage.memory import (
    DisabledEventIsolation,
    MemoryStorage,
    SimpleEventIsolation,
)
from mocked_bot import MockedBot

DATA_DIR = Path(__file__).parent / "data"

CHAT_ID = -42
USER_ID = 42

SKIP_MESSAGE_PATTERN = 'Need "--{db}" option with {db} URI to run'
INVALID_URI_PATTERN = "Invalid {db} URI {uri!r}: {err}"


def pytest_addoption(parser):
    parser.addoption("--redis", default=None, help="run tests which require redis connection")
    parser.addoption("--mongo", default=None, help="run tests which require mongo connection")


def pytest_configure(config):
    config.addinivalue_line("markers", "redis: marked tests require redis connection to run")
    config.addinivalue_line("markers", "mongo: marked tests require mongo connection to run")

    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    else:
        asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())



@pytest_asyncio.fixture()
async def memory_storage():
    storage = MemoryStorage()
    try:
        yield storage
    finally:
        await storage.close()


@pytest_asyncio.fixture()
async def lock_isolation():
    isolation = SimpleEventIsolation()
    try:
        yield isolation
    finally:
        await isolation.close()


@pytest_asyncio.fixture()
async def disabled_isolation():
    isolation = DisabledEventIsolation()
    try:
        yield isolation
    finally:
        await isolation.close()


@pytest.fixture()
def bot():
    return MockedBot()


@pytest.fixture(name="storage_key")
def create_storage_key(bot: MockedBot):
    return StorageKey(chat_id=CHAT_ID, user_id=USER_ID, bot_id=bot.id)


@pytest_asyncio.fixture()
async def dispatcher():
    dp = Dispatcher()
    await dp.emit_startup()
    try:
        yield dp
    finally:
        await dp.emit_shutdown()


# @pytest.fixture(scope="session")
# def event_loop_policy(request):
#     if sys.platform == "win32":
#         return asyncio.WindowsSelectorEventLoopPolicy()
#     return asyncio.DefaultEventLoopPolicy()