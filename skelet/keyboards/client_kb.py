from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
b1 = KeyboardButton('/Режим_Работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Меню')
b4 = KeyboardButton('Отправить свой номер телефона', request_contact=True)
b5 = KeyboardButton('Отправить свое местоположение', request_location=True)

b6 = KeyboardButton('/Админ_панель')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b3).row(b1, b2).row(b4, b5).add(b6)