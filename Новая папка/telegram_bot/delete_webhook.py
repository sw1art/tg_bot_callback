from aiogram import Bot
from core.settings import settings
import asyncio

async def delete_webhook():
    bot = Bot(token=settings.TELEGRAM_TOKEN)
    webhook_info = await bot.get_webhook_info()
    print(f"Current webhook info: {webhook_info}")

    await bot.delete_webhook()
    print("Webhook deleted successfully!")
    await bot.session.close()

if __name__ == "__main__":
    asyncio.run(delete_webhook())
