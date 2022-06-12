import token
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes


async def hello(update: Update, context: callbackcontext) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = token("5540059839:AAFDvmLZ7lLmZHpeL9kLm3YHtWsUNazFGa0").build()

app.add_handler(CommandHandler("hello", hello))

print('server start')
app.run_polling()