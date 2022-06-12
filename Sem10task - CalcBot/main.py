
import telebot
import config

# Создаем экземпляр бота
bot = telebot.TeleBot(config.token)
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])

def start(m, res=False):
    bot.send_message(m.chat.id, 'Я бот-калькулятор.\nВведите выражение для расчёта через пробел, например 25 + 17\n ')

# Получение сообщений от юзера
# @bot.message_handler(content_types=["text"])
@bot.message_handler(func=lambda m: True)


# def handle_text(message):

def calculate(message):

    data = list(message.text.split())
 

    operand2 = data.pop()
    operation = data.pop()
    operand1 = data.pop()
    
# Проверка на коплексное число

    if operand1.find('j') != -1: operand1 = complex(operand1) 
    else: operand1 = float(operand1)
    
    if operand2.find('j') != -1: operand2 = complex(operand2) 
    else: operand2 = float(operand2)


    result = 0
    if operation == '+':
        result = operand1 + operand2
    if operation == '-':
        result = operand1 - operand2
    if operation == '/':
        result = operand1 / operand2
    if operation == '*':
        result = operand1 * operand2
    reply_message = (f"{operand1} {operation} {operand2} = {result}")

    bot.send_message(message.chat.id, 'Решаю выражение' + reply_message)

# Запускаем бота
bot.polling(none_stop=True, interval=0)