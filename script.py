
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, CallbackContext
import logging
import random
import datetime
import time

a_file = open("foresights.txt", encoding='UTF-8')
file_contents = a_file.read()
contents_split = file_contents.split('.')

a_file.close()
users_list = {
    "@pasha1561": 915489577
    , '@ira_hrdv': 455735498
    , '@ura': 1316194498
    , '@anastasia_preveda': 807119959
    , '@iryna_volodymyrivna': 651780710
    , '@tanya': 818234057
    , '@dmytro': 519468181
    , '@ira_nasti': 812350065
    , '@solomiya': 1179292720
    , '@ira_sestra': 1152054114
}


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
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(update.effective_chat.id) + ' \n ' + str(datetime.datetime.now()))  # str(datetime.datetime.now())) #update.message.text)


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)


while 1 == 1:
    # def once(context: CallbackContext):
    #     message = random.choice(contents_split).strip()
    #     context.bot.send_message(chat_id=915489577, text=message)
    #     # for user in users_list.values():
    #     #     message = random.choice(contents_split).strip()
    #     #     context.bot.send_message(chat_id=user, text=message)
    #
    #
    # j.run_once(once, 2)
    context_ = CallbackContext(dispatcher)

    def daily_suggestion(context: CallbackContext):
        for user in users_list.values():
            # if datetime.date(2022, 2, 10) == datetime.date.today():
            #     if user == 915489577:
            #         message = 'Бот заїбав \n І передбачення: \n ' + random.choice(contents_split).strip()
            #         context.bot.send_message(chat_id=user, text=message)
            # #     elif user == 455735498:
            # #         message = 'Іра, дивимось сьогодні гру престолів) \n І передбачення: \n ' + random.choice(contents_split).strip()
            #     elif user == 1316194498:
            #         message = 'Юра, маєш файну шкодовку) \n І передбачення: \n ' + random.choice(contents_split).strip()
            #         context.bot.send_message(chat_id=user, text=message)
            #     elif user == 807119959:
            #         message = 'Настя, ти купила свічки? \n І передбачення: \n ' + random.choice(contents_split).strip()
            #     elif user == 651780710:
            #         message = 'Іра, не переживай, в тебе все вийде) \n І передбачення: \n ' + random.choice(contents_split).strip()
            #     elif user == 818234057:
            #         message = 'Єржан, вставай) \n І передбачення: \n ' + random.choice(contents_split).strip()
            #     elif user == 519468181:
            #         message = 'Дмитре, ніхуя собі блять маєш вихідний) \n І передбачення: \n ' + random.choice(contents_split).strip()
            # else:
            #     message = random.choice(contents_split).strip()
            message = random.choice(contents_split).strip()
            context.bot.send_message(chat_id=user, text=message)


    if datetime.datetime.now().hour == 7 and datetime.datetime.now().minute == 00:
        daily_suggestion(context_)
        time.sleep(4000)

    # job_daily = j.run_daily(daily_suggestion, days=(0, 1, 2, 3, 4, 5, 6), time=datetime.time(hour=21, minute=52, second=00)) # -2 hours

    # time.sleep(20)
    # time.sleep(86400)
