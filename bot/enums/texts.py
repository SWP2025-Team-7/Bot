from enum import Enum

class ButtonsText(Enum):
    confirm = "Подтвердить"
    decline = "Отклонить"

class MessagesText(Enum):
    start_message = """
    Это бот для подачи справок с места работы, для работы введите /send
    """
    send_instructions = """
    Отправьте вашу справку в формате pdf
    """
    error_message = """
    К сожалению, в данный момент сервис недоступен, свяжитесь с администратором
    """
    waiting_data_extraction = """
    Извлекаем данные, ожидайте
    """