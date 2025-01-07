from aiogram import types

async def instructions_info(message: types.Message):
    await message.answer(
        "Инструкции для клиентов:\n\n"
        "- Использование товара.\n"
        "- Уход за товаром.\n"
        "- Часто задаваемые вопросы (FAQ).\n\n"
        "Для получения конкретной инструкции, выберите ее в нашем меню."
    )
