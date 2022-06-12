from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
import main as m
# from spy import *

def hi_command(update: Update, context: CallbackContext):
    m.log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}!')
def help_command(update: Update, context: CallbackContext):
    m.log(update, context)
    update.message.reply_text(f'/hi\n/time\n/help')
def time_command(update: Update, context: CallbackContext):
    m.log(update, context)
    update.message.reply_text(f'{datetime.datetime.now().time()}')
def sum_command(update: Update, context: CallbackContext):
    m.log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() # /sum 123 534543
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x+y}')



updater = Updater("5540059839:AAFDvmLZ7lLmZHpeL9kLm3YHtWsUNazFGa0")
updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
print('server start')
updater.start_polling()
updater.idle()
