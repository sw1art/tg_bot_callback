import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from core.settings import settings
from telegram_bot.handlers import register_handlers

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Создаем бота и диспетчер
bot = Bot(token=settings.TELEGRAM_TOKEN)
dp = Dispatcher()

# Регистрируем хендлеры
register_handlers(dp)

# Запуск polling
async def main():
    logger.info("Starting bot...")
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Error in polling: {e}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
