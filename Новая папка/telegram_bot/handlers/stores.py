from aiogram import types

async def site(message: types.Message):
    await message.answer(
        "Наш магазин:\n"
        "👉 [Перейти](https://triple-vision.ru/),\n\n"
        "Для возврата в меню нажмите /menu.",
        parse_mode="Markdown",
    )

async def yandex_market(message: types.Message):
    await message.answer(
        "Наш магазин на Яндекс.Маркет:\n"
        "👉 [Перейти](https://market.yandex.ru/),\n\n"
        "Для возврата в меню нажмите /menu.",
        parse_mode="Markdown",
    )

async def ozone_store(message: types.Message):
    await message.answer(
        "Наш магазин на Озон:\n"
        "👉 [Перейти](https://www.ozon.ru/),\n\n"
        "Для возврата в меню нажмите /menu.",
        parse_mode="Markdown",
    )

async def wildberries_store(message: types.Message):
    await message.answer(
        "Наш магазин на Вайлдберис:\n"
        "👉 [Перейти](https://www.wildberries.ru/),\n\n"
        "Для возврата в меню нажмите /menu.",
        parse_mode="Markdown",
    )


async def avito_store(message: types.Message):
    await message.answer(
        "Наш магазин на Авито:\n"
        "👉 [Перейти](https://www.avito.ru/),\n\n"
        "Для возврата в меню нажмите /menu.",
        parse_mode="Markdown",
    )
