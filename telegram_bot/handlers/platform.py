from aiogram import types


"""
Для каждой площадки можно вставить URL средствами языка Markdown
"""

async def yandex_market_handler_platform(message: types.Message):
    await message.answer(
        "Если заказ был с Яндекс Маркета, напишите номер заказа: ",
        parse_mode="Markdown",
    )

async def ozone_store_handler_platform(message: types.Message):
    await message.answer(
        "Если заказ был с Озона, напишите номер заказа: ",
        parse_mode="Markdown",
    )

async def wildberries_store_handler_platform(message: types.Message):
    await message.answer(
        "Если заказ был с Вайлдберис, напишите номер заказа: ",
        parse_mode="Markdown",
    )
    
async def avito_store_handler_platform(message: types.Message):
    await message.answer(
        "Если заказ был с Авито, напишите номер заказа: ",
        parse_mode="Markdown",
    )

async def site_handler_platform(message: types.Message):
    await message.answer(
        "Если заказ был с Нашего сайта, напишите номер заказа: ",
        parse_mode="Markdown",
    )