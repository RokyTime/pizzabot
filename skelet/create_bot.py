from aiogram import Bot
from aiogram.dispatcher import Dispatcher

import os

bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher(bot)