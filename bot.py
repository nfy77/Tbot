import asyncio
import logging
import sqlite3

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.contrib.fsm_storage.memory import MemoryStorage
#from aiogram.utils import executor

from app.config_reader import load_config
from app.handlers.common import register_handlers_common
from app.handlers.registration import register_handlers_registration
from app.handlers.horodru import register_handlers_horodru
from app.handlers.beckscale import register_handlers_beckscale

from app.db.db_map import create_user_table, create_file_table

from datetime import datetime
from ftplib import FTP

logger = logging.getLogger(__name__)

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Старт"),
        BotCommand(command="/registration", description="Регистрация"),
        BotCommand(command="/horodru", description="Гороскоп Друидов"),
        BotCommand(command="/beckscale", description="Шкала депрессии Бека"),
        BotCommand(command="/cancel", description="Отменить текущее действие")
    ]
    await bot.set_my_commands(commands)

async def main():
    # Настройка логирования в stdout
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.info("Starting bot")

    # Парсинг файла конфигурации
    config = load_config("config/bot.ini")

    # Объявление и инициализация объектов БД
    # подключение к бд
    connect = sqlite3.connect(config.tg_bot.db_path)
    cursor = connect.cursor()
    # создание таблиц
    create_user_table(connect, cursor)
    
    # Объявление и инициализация объектов бота и диспетчера
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher(bot, storage=MemoryStorage())

    # Регистрация хэндлеров
    register_handlers_common(dp, config.tg_bot.admin_id)
    register_handlers_registration(dp, connect, cursor)
# TODO гороскоп и карта    
    register_handlers_horodru(dp, connect, cursor)
    register_handlers_beckscale(dp, connect, cursor)

    # Установка команд бота
    await set_commands(bot)

    # Запуск поллинга
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())