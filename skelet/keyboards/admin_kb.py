from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
b1 = KeyboardButton('/Добавить_пункт_меню')
b2 = KeyboardButton('/Отмена')





kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)

kb_admin.add(b1).add(b2)