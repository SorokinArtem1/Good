from langchain_ollama import OllamaLLM

model = OllamaLLM(model="llama3")




import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
import requests
import json

# Задаем токен для вашего Telegram-бота
API_TOKEN = '7154115448:AAH-ThqJTkgWVE8ZxqQHhZXPr-hQEMGsNFU'

# Настраиваем логирование
logging.basicConfig(level=logging.INFO)

# Инициализируем бота и диспетчер
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


# Хэндлер для команды /start
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    """ Приветственное сообщение и запрос текста от пользователя """
    await message.answer("Что хотите узнать?")


# Хэндлер для обработки любых сообщений
@dp.message()
async def handle_message(message: types.Message):
    """ Обработка сообщения пользователя и генерация ответа с помощью модели Ollama """
    user_input = message.text
    await message.answer("Думаю...")

    try:
        result = model.invoke(input = user_input)
        await message.answer(result)
    except Exception as e:
        logging.error(f"Ошибка при обращении к модели: {e}")
        await message.answer("Произошла ошибка при обработке вашего запроса. Попробуйте позже.")

result = model.invoke(input="hello world")

print (result)
async def main():
    # Запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
