# import requests
#
# API_link = 'https://api.telegram.org/bot1597557831:AAErd2hvgAyZpYwV7PMIMs1z7CBlnx5cz9M'
#
# updates = requests.get(API_link + '/getUpdates?offset=-1').json()
#
#
# print(updates)
#
# message_from_user = updates['result'][0]['message']
# chat_id_user = message_from_user['from']['id']
# text_from_user = message_from_user['text']
#
# sendMessage = requests.get(API_link + f'/sendMessage?chat_id={chat_id_user}&text=Привет,'
#                                       f' ты написал мне это: {text_from_user}')
import asyncio
from aiogram import Dispatcher, Bot, executor
from confing import TG_TOKEN

loop = asyncio.get_event_loop()
bot = Bot(TG_TOKEN, parse_mode='HTML')
dispatcher = Dispatcher(bot=bot, loop=loop)

if __name__ == '__main__':
    from handlers import dispatcher
    from handlers import send_message_admin
    executor.start_polling(dispatcher=dispatcher, on_startup=send_message_admin)
    print(send_message_admin)

