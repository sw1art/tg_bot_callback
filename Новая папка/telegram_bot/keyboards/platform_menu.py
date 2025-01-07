from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Клавиатура для выбора площадки
platform_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Я.Маркет"), KeyboardButton(text="Озон")],
        [KeyboardButton(text="Вайлдберис"), KeyboardButton(text="Авито")],
        [KeyboardButton(text="Наш сайт"), KeyboardButton(text="Назад")],
    ],
    resize_keyboard=True,
)