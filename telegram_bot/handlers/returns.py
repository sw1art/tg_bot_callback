from aiogram import types
from telegram_bot.keyboards.returns_menu import returns_menu
from telegram_bot.keyboards.platform_menu import platform_menu

# Обработка выбора причины возврата
async def incomplete_package_handler(message: types.Message):
    await message.answer(
        "Неполная комплектация: в посылке чего-то не хватает.\n"
        "Выберите, на какой площадке вы оформили заказ:",
        reply_markup=platform_menu,
    )

async def damaged_delivery_handler(message: types.Message):
    await message.answer(
        "Повреждение при доставке: товар пришёл с дефектами или повреждениями.\n"
        "Выберите, на какой площадке вы оформили заказ:",
        reply_markup=platform_menu,
    )

async def delayed_delivery_handler(message: types.Message):
    await message.answer(
        "Задержка доставки: заказ пришёл позже обещанного срока.\n"
        "Выберите, на какой площадке вы оформили заказ:",
        reply_markup=platform_menu,
    )

async def not_working_handler(message: types.Message):
    await message.answer(
        "Товар не работает: устройство или аксессуар оказался неисправным.\n"
        "Выберите, на какой площадке вы оформили заказ:",
        reply_markup=platform_menu,
    )

async def wrong_item_handler(message: types.Message):
    await message.answer(
        "Ошибочная отправка: вместо заказанного товара пришёл другой.\n"
        "Выберите, на какой площадке вы оформили заказ:",
        reply_markup=platform_menu,
    )

# Обработка кнопки "Назад" для возврата в меню выбора причины
async def back_to_reasons_handler(message: types.Message):
    await message.answer(
        "Возвращаемся к выбору причины возврата:",
        reply_markup=returns_menu,
    )