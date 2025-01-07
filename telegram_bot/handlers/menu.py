from aiogram import types
from telegram_bot.keyboards.main_menu import main_menu

async def start_menu(message: types.Message):
    await message.answer(
        "Добро пожаловать! Выберите один из разделов ниже:",
        reply_markup=main_menu,
    )
