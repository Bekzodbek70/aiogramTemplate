from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu=ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='Python'),
            KeyboardButton(text='Telegram Bot'),
        ],
    ],
    resize_keyboard=True
)