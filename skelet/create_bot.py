from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()

import os

bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher(bot, storage=storage)