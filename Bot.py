import telegram
from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import MessageFilter
from telegram.ext import MessageHandler
from telegram.ext import Filters

TG_TOKEN = '1431176914:AAF_wC3D3fykN0rLl1ykBBObO1I9gLEtS2s'


def message_handler(bot: Bot, update: Update):
    user = update.effective_user
    if user:
        name = user.first_name
    else:
        name = 'anonim'

    text = update.effective_message.text
    reply_text = f'Привет, {name}!\n\n{text}!'

    bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=reply_text
    )


def main():
    bot = Bot(
        token=TG_TOKEN
    )
    updater = Updater(
        bot=bot, use_context=True
    )

    handler = MessageHandler(Filters.all, message_handler)
    updater.dispatcher.add_handler(handler=handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
