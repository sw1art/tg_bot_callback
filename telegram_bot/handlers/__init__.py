from aiogram import Dispatcher, F
from telegram_bot.handlers.menu import start_menu
from telegram_bot.handlers.returns import (
    returns_menu_handler,
    incomplete_package_handler,
    damaged_delivery_handler,
    delayed_delivery_handler,
    not_working_handler,
    wrong_item_handler,
    back_to_main_menu_handler,
)
from telegram_bot.handlers.instructions import instructions_info
from telegram_bot.handlers.stores import (
    yandex_market, 
    ozone_store, 
    wildberries_store, 
    avito_store, 
    site
)

from telegram_bot.handlers.about import about_us

def register_handlers(dp: Dispatcher):
    """
    Регистрация всех хендлеров.
    """
    # Главное меню
    dp.message.register(start_menu, F.text.in_({"start", "menu"}))

    # Разделы меню
    dp.message.register(returns_menu_handler, F.text == "Возвраты")
    dp.message.register(instructions_info, F.text == "Инструкции")
    dp.message.register(site, F.text == "Наш сайт")
    dp.message.register(yandex_market, F.text == "Мы на Я.Маркет")
    dp.message.register(ozone_store, F.text == "Мы на Озон")
    dp.message.register(wildberries_store, F.text == "Мы на Вайлдберис")
    dp.message.register(avito_store, F.text == "Мы на Авито")
    dp.message.register(about_us, F.text == "О нас")

    # Возвраты
    dp.message.register(incomplete_package_handler, F.text == "Неполная комплектация")
    dp.message.register(damaged_delivery_handler, F.text == "Повреждение при доставке")
    dp.message.register(delayed_delivery_handler, F.text == "Задержка доставки")
    dp.message.register(not_working_handler, F.text == "Товар не работает")
    dp.message.register(wrong_item_handler, F.text == "Ошибочная отправка")
    dp.message.register(back_to_main_menu_handler, F.text == "Назад")

    # Площадки
    dp.message.register(yandex_market, F.text == "Я.Маркет")
    dp.message.register(ozone_store, F.text == "Озон")
    dp.message.register(wildberries_store, F.text == "Вайлдберис")
    dp.message.register(avito_store, F.text == "Авито")
    dp.message.register(avito_store, F.text == "Наш сайт")