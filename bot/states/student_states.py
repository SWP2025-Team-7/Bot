from aiogram.fsm.state import State, StatesGroup

class StudentStates(StatesGroup):
    start = State()
    language = State()
    send = State()
    login = State()
    confirm = State()
