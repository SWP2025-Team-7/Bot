from aiogram.fsm.state import State, StatesGroup

class States(StatesGroup):
    start = State()
    default = State()
    language = State()
    send = State()
    login = State()
    confirm = State()
