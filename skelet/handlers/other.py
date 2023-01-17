from aiogram import types, Dispatcher

from create_bot import dp

import json
import string


#@dp.message_handler()
async def swearing_filter(message : types.Message):
    if {i.lower().translate(str.maketrans("", "", string.punctuation)) for i in message.text.split(" ")}\
        .intersection(set(json.load(open("cenz.json")))) != set():
        await message.reply("Маты запрещены.")
        await message.delete()



def register_handler_other(dp : Dispatcher):
    dp.register_message_handler(swearing_filter)