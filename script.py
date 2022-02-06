from pytz import unicode
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, CallbackContext
import logging
import random
# import redis
import datetime


a_file = open("foresights.txt", encoding='UTF-8')
file_contents = a_file.read()
contents_split = file_contents.split('.')

a_file.close()
# contents_split = all_foresights.split('.')
users_list = ['@pasha1561', '@ira_hrdv']

updater = Updater(token='5200494282:AAFtQ8PJM3Tm7jxgMpd4x1KHYGU-3UafZ0s', use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

j = updater.job_queue


def start(update, context):
    message = random.choice(contents_split).strip()
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)


def daily_suggestion(context: CallbackContext):
    for user in users_list:
        message = random.choice(contents_split).strip()
        context.bot.send_message(chat_id=user, text=message)


job_daily = j.run_daily(daily_suggestion, days=(0, 1, 2, 3, 4, 5, 6), time=datetime.time(hour=12, minute=00, second=00))
