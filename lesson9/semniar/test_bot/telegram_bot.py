from aiogram import Bot, types, Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv, find_dotenv #библиотека для работы с виртуальным окружением
import requests
import os

load_dotenv(find_dotenv()) #поиск файла с токеном

bot = Bot(os.getenv('TOKEN'))


dp = Dispatcher(bot)

async def on_startup(_):
    print("online!")

@dp.message_handler()
async def echo_send(message: types.Message):
    await message.reply("Hi!")

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)



url_api = "https://api.telegram.org/bot5930634936:AAEb5i1G9q3QWqSVJ2xRoOs1FrJjJ4GtApY"
updates = requests.get(url_api + "/getUpdates").json()
print(updates)