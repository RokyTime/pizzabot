from aiogram.utils import executor

from create_bot import dp


from handlers import client, admin, other

async def on_startup(_):
    print("Бот онлайн") 


other.register_handler_other(dp)


executor.start_polling(dp, skip_updates=False, on_startup=on_startup)