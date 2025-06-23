from enums import Messages, Languages, Buttons
import logging 

russian_pack = {
    Messages.LANGUAGE: "Выберите язык:",
    Messages.LANGUAGE_CHANGED: "Язык изменен на русский",
    Messages.ERROR: "Извините(",
    Messages.LOGIN: "Innopolis SSO",
    Messages.CANCEL: "Действие прервано",
    Messages.INSTRUCTIONS: "/login чтобы авторизоваться с помощью университетского SSO\n/send чтобы отправить документ\n/language чтобы изменить язык\n/cansel чтобы прервать действие",
    Messages.SEND: "Отправьте документ"
}

english_pack = {
    Messages.LANGUAGE: "Choose language:",
    Messages.LANGUAGE_CHANGED: "Language changed to English",
    Messages.ERROR: "Sorry(",
    Messages.LOGIN: "Innopolis SSO",
    Messages.CANCEL: "Activity interrupt",
    Messages.INSTRUCTIONS: "/login to login with university sso\n/send to send document\n/language to change language\n/cancel to interrupt activity",
    Messages.SEND: "Send document"
}

buttons_russian_pack = {
    Buttons.CONFIRM: "Подтвердить",
    Buttons.DECLINE: "Отклонить",

    Buttons.RUSSIAN: "Русский",
    Buttons.ENGLISH: "Английский",

    Buttons.LOGIN: "Вход"
}

buttons_english_pack = {
    Buttons.CONFIRM: "Confirm",
    Buttons.DECLINE: "Decline",

    Buttons.RUSSIAN: "Russian",
    Buttons.ENGLISH: "English",

    Buttons.LOGIN: "Login"
}

def get_message(message: Messages, language: Languages = Languages.ENG):
    match language:
        case Languages.RU:
            return russian_pack.get(message)
        case Languages.ENG:
            return english_pack.get(message)
        case _:
            return english_pack.get(message)
        
def get_button_text(button: Buttons, language: Languages = Languages.ENG):
    match language:
        case Languages.RU:
            return buttons_russian_pack.get(button)
        case Languages.ENG:
            return buttons_english_pack.get(button)
        case _:
            return buttons_english_pack.get(button)
