from aiogram import types, Dispatcher

from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove

async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита!', reply_markup=kb_client)
    except:
        await message.reply('Мне можно написать только в личные сообщения.')


async def pizza_open_command(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Вс-Чт: 9:00-20:00,\nПт-Сб 10:00-23:00.', reply_markup=kb_client)
    except:
        await message.reply('Мне можно написать только в личные сообщения.') 


async def pizza_place_command(message : types.message):
    try:
        await bot.send_message(message.from_user.id, 'Улица бана №15.', reply_markup=kb_client)
    except:
        await message.reply('Мне можно написать только в личные сообщения.') 


def register_handler_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Расположение'])