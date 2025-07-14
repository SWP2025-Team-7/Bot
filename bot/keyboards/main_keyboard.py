from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from bot.texts import get_button_text
from bot.enums import Buttons, Languages

def get_main_keyboard(language: Languages = Languages.ENG):
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=get_button_text(language=language, button=Buttons.SEND))
            ],
            [
                KeyboardButton(text=get_button_text(language=language, button=Buttons.LANGUAGE))
            ]
        ]
    )