import os
from dotenv import load_dotenv

# Загрузка .env файла
load_dotenv()

class Settings:
    # Telegram Bot
    TELEGRAM_TOKEN: str = os.getenv("TELEGRAM_TOKEN")
    WEBHOOK_URL: str = os.getenv("WEBHOOK_URL")

    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    # Additional settings
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    APP_ENV: str = os.getenv("APP_ENV", "development")  # default: development

# Создаем экземпляр для использования в проекте
settings = Settings()
