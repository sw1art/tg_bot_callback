from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Главное меню
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Возвраты"),
            KeyboardButton(text="Инструкции"),
        ],
        [
            KeyboardButton(text="Я.Маркет"),
            KeyboardButton(text="Озон"),
        ],
        [
            KeyboardButton(text="Вайлдберис"),
            KeyboardButton(text="Авито"),
        ],
        [   
            KeyboardButton(text="Наш сайт"),
            KeyboardButton(text="О нас"),
        ],
    ],
    resize_keyboard=True,
)
