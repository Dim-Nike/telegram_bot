from main import bot, dispatcher

from aiogram.types import Message
from confing import chat_id_admin
from confing import chat_id_user_1
from confing import chat_id_user_2

async def send_message_admin(dispatcher):
    await bot.send_message(chat_id=chat_id_user_1, text='Бот готов к работе')

@dispatcher.message_handler()
async def echo(message: Message):
    text = f'Псс, работа не нужна?'
    await bot.send_message(chat_id=message.from_user.id, text=text)

    # await message.answer(text=text)