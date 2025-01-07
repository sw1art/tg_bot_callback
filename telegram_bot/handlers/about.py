from aiogram import types


async def about_us(message: types.Message):
    await message.answer(
        "О нашей компании:\n\n"
        "Мы стремимся предоставлять лучший сервис для наших клиентов на всех "
        "торговых площадках. Возвращайтесь к нам снова!\n\n"
        "Для возврата в меню нажмите /menu."
    )
