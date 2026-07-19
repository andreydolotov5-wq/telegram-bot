bot.py
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "8066556835:AAFdYrMtni9C4Qtc6o24A3jhRqkHW8dJwmk"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("Privet, ya bot!")

@dp.message(Command("help"))
async def help_cmd(message: types.Message):
    await message.answer("Napishi /start")

async def main():
    await dp.start_polling(bot)

if name == "main":
    asyncio.run(main())
