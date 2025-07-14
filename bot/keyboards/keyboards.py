from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    WebAppInfo,
)

from bot.enums import CallBacks
from bot.texts import get_button_text, Languages, Buttons

def get_confirmation_keyboard(language: Languages = Languages.ENG) -> InlineKeyboardMarkup:
    data_confirmation_kb = [
        [InlineKeyboardButton(text=get_button_text(language=language, button=Buttons.CONFIRM), callback_data=CallBacks.confirm.value),
         InlineKeyboardButton(text=get_button_text(language=language, button=Buttons.DECLINE), callback_data=CallBacks.decline.value)]
    ]

    return InlineKeyboardMarkup(inline_keyboard=data_confirmation_kb)

def get_language_keyboard(language: Languages = Languages.ENG) -> InlineKeyboardMarkup:
    language_choose_kb = [
        [InlineKeyboardButton(text=get_button_text(language=language, button=Buttons.RUSSIAN), callback_data=CallBacks.ru.value),
        InlineKeyboardButton(text=get_button_text(language=language, button=Buttons.ENGLISH), callback_data=CallBacks.eng.value)]
    ]

    return InlineKeyboardMarkup(inline_keyboard=language_choose_kb)

def get_login_keyboard(language: Languages = Languages.ENG) -> InlineKeyboardMarkup:
    login_kb = [
        [InlineKeyboardButton(text=get_button_text(language=language, button=Buttons.LOGIN), web_app=WebAppInfo(url="https://innopolis.university/"))]
    ]

    return InlineKeyboardMarkup(inline_keyboard=login_kb) 