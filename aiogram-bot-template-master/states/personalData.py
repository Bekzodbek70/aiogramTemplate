from aiogram.dispatcher.filters.state import StatesGroup, State

class Personaldata(StatesGroup):
    fullname=State()
    email=State()
    phone=State()
