from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Клавиатура для меню Возвратов
returns_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Неполная комплектация")],
        [KeyboardButton(text="Повреждение при доставке")],
        [KeyboardButton(text="Задержка доставки")],
        [KeyboardButton(text="Товар не работает")],
        [KeyboardButton(text="Ошибочная отправка")],
        [KeyboardButton(text="Назад")],
    ],
    resize_keyboard=True,
)
