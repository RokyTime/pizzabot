from aiogram.utils import executor

from create_bot import dp

from data_base.sqlite_db import sql_start
from handlers import client, admin, other

async def on_startup(_):
    print("Бот онлайн")
    sql_start()


admin.register_handler_admin(dp)
client.register_handler_client(dp)
other.register_handler_other(dp)



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)