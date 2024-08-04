import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
import os
import random
import asyncio

# Загрузка переменных окружения
load_dotenv()

# Инициализация бота и диспетчера
TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def send_welcome(message: Message):
    await message.answer(f"Hello, {message.from_user.first_name}!")

# Обработчик команды /myinfo
@dp.message(Command("myinfo"))
async def send_info(message: Message):
    user = message.from_user
    await message.answer(f"Your id: {user.id}\nYour name: {user.first_name}\nYour username: {user.username}")


@dp.message(Command("random_recipe"))
async def send_recipe(message: Message):
    recipes = [
        "Рецепт 1: Смешайте муку, яйца и сахар. Выпекать при температуре 180°C 25 минут.",
        "Рецепт 2: Сварите макароны, затем добавьте томатный соус и сыр.",
        "Рецепт 3: Курицу гриль с солью и перцем.",
        "Рецепт 4: Приготовьте салат из салата, помидоров и огурцов.",
        "Рецепт 5: Обжарьте лук и чеснок, затем добавьте говядину и готовьте до готовности."
    ]
    recipe = random.choice(recipes)
    await message.answer(recipe)


async def main():
    logging.basicConfig(level=logging.INFO)
    try:

        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == '__main__':
    asyncio.run(main())
