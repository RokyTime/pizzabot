from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from create_bot import dp, bot
from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from keyboards import kb_admin, kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base.sqlite_db import sql_add, sql_read2, delete_function
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



admin_ID = [1996472029]



class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

async def make_changes_command(message : types.Message):
    global admin_ID
    if message.from_user.id in admin_ID:
        await bot.send_message(message.from_user.id, '...', reply_markup=ReplyKeyboardRemove())
        await bot.send_message(message.from_user.id, 'Панель настройки.', reply_markup=kb_admin)
    else:
        await bot.send_message(message.from_user.id, 'Вы не являетесь администратором.')



#@dp.message_handler(commands=['Добавить_пункт_меню'], state=None)
async def cm_start(message : types.Message):
    if message.from_user.id in admin_ID:
        await FSMAdmin.photo.set()
        await message.reply('Загрузи фото.')


#dp.message_handler(state='*', commands=['Отмена'])
#dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_handler(message : types.message, state=FSMContext):
    if message.from_user.id in admin_ID:
        await bot.send_message(message.from_user.id, 'Ok.', reply_markup=ReplyKeyboardRemove())
        await bot.send_message(message.from_user.id, 'Отменено.', reply_markup=kb_client)
        current_state = await state.get_state()
        if current_state == None:
            return
        else:
            await state.finish()
        



#@dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message : types.Message, state=FSMContext):
    if message.from_user.id in admin_ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply('Теперь введи название.')

#@dp.message_handler(state=FSMAdmin.name)
async def load_name(message : types.Message, state=FSMContext):
    if message.from_user.id in admin_ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply('Теперь введи описание.')

#@dp.message_handler(state=FSMAdmin.description)
async def load_description(message : types.Message, state=FSMContext):
    if message.from_user.id in admin_ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        await message.reply('Теперь введи цену.')


#@dp.message_handler(state=FSMAdmin.price)
async def load_price(message : types.Message, state=FSMContext):
    if message.from_user.id in admin_ID:
        async with state.proxy() as data:
            try:
                data['price'] = float(message.text)
                #await message.reply(str(data))
            except:
                await message.reply('Нужно ввести только число.\nДобавь пункт в меню заново.')
                await state.finish()
        try:
            await sql_add(state)
            await state.finish()
            await message.reply('Добавлено успешно.')
        except:
            await message.reply('Ошибка в бае данных.\nПопробуй ещё раз.\nВозможно, такое имя уже существует.')


async def del_callback(callback : types.CallbackQuery):
    await delete_function(callback.data.replace('delete ', ''))
    await callback.answer(text=f'{callback.data.replace("delete ", "")} удалена', show_alert=True)

async def delete_from_menu(message : types.Message):
    if message.from_user.id in admin_ID:
        read = await sql_read2()
        for ret in read:
            await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание:\n{ret[2]}\nЦена:{ret[3]} руб.')
            await bot.send_message(message.from_user.id, '^^^', reply_markup=InlineKeyboardMarkup().\
                add(InlineKeyboardButton(text=f'Удалить {ret[1]}', callback_data=f'delete {ret[1]}')))
            

def register_handler_admin(dp : Dispatcher):
    dp.register_message_handler(make_changes_command, commands=['Админ_панель'])
    dp.register_message_handler(cm_start, commands=['Добавить_пункт_меню'], state=None)
    dp.register_message_handler(cancel_handler, state='*', commands=['Отмена'])
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state='*')
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(delete_from_menu, commands=['Удалить'])
    dp.register_callback_query_handler(del_callback, Text(startswith='delete '))