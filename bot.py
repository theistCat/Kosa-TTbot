import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from database import Database
from handlers import common, admin, executor

API_TOKEN = "7974083015:AAGv7PustiY-eJfDtT2q9ZSE6r2t9SLTS80"
# API_TOKEN = "7300885902:AAHp99Wki_VnVmKco65G4uj7DUyXm2h880A"

DB_PATH = "database.db"  # Путь к базе данных
bot = Bot(token=API_TOKEN)

async def main():
    dp = Dispatcher(storage=MemoryStorage())

    # Подключение базы данных
    db = Database(DB_PATH)

    # Регистрация обработчиков
    dp.include_router(common.router)
    dp.include_router(admin.router)
    dp.include_router(executor.router)

    # Передача базы данных в хендлеры
    dp["db"] = db

    # Запуск бота
    try:
        print("Бот запущен!")
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
