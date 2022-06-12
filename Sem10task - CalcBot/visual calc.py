# Прикрутить бота к задаче с предыдущего семинара:
#     a). Создать калькулятор для работы с рациональными и комплексными числами, организовать меню

# Визуальный калькулятор с рациональными числами


# Импорт библиотек и исходные данные
# Создаем окно приложения  — объект Tk с заголовком Calculator.
# Во вложенном кортеже buttons будут храниться обозначения для кнопок. 
# В список stack будем добавлять введенные числа и операции, которые надо совершить. 
# activeStr предназначен для хранения набираемого числа.

from tkinter import *
from decimal import *

root = Tk()
root.title('Calculator')

buttons = (('7', '8', '9', '/', '4'),
           ('4', '5', '6', '*', '4'),
           ('1', '2', '3', '-', '4'),
           ('0', '.', '=', '+', '4')
           )

activeStr = ''
stack = []


# Функция calculate получает из списка stack операнды и операцию которую над ними надо произвести. 
# Результат отображается в надписи label. 
# Получать из списка строки будем с помощью метода pop.

def calculate():
    global stack
    global label
    result = 0
    operand2 = Decimal(stack.pop())
    operation = stack.pop()
    operand1 = Decimal(stack.pop())

    if operation == '+':
        result = operand1 + operand2
    if operation == '-':
        result = operand1 - operand2
    if operation == '/':
        result = operand1 / operand2
    if operation == '*':
        result = operand1 * operand2
    label.configure(text=str(result))


# В функции click выполняется обработка нажатой клавиши.
# В качестве ее аргумента передается текст, отображаемый на кнопке, которую нажали. 

def click(text):
    global activeStr
    global stack
    if text == 'CE':
        stack.clear()
        activeStr = ''
        label.configure(text='0')
    elif '0' <= text <= '9':
        activeStr += text
        label.configure(text=activeStr)
    elif text == '.':
        if activeStr.find('.') == -1:
            activeStr += text
            label.configure(text=activeStr)
    else:
        if len(stack) >= 2:
            stack.append(label['text'])
            calculate()
            stack.clear()
            stack.append(label['text'])
            activeStr = ''
            if text != '=':
                stack.append(text)
        else:
            if text != '=':
                stack.append(label['text'])
                stack.append(text)
                activeStr = ''
                label.configure(text='0')

# Внешний вид
# Теперь займемся оформлением внешнего вида калькулятора и зададим обработку нажатия кнопок. 
# Создаем надпись для вывода набираемых значений и результатов. 
# В цикле создаем кнопки. 
# Расположение кнопок и надписи осуществляется в табличном виде с помощью упаковщика grid. 
# И в завершении запускаем цикл обработки событий mainloop.

label = Label(root, text='0', width=35)
label.grid(row=0, column=0, columnspan=4, sticky="nsew")

button = Button(root, text='CE', command=lambda text='CE': click(text))
button.grid(row=1, column=3, sticky="nsew")
for row in range(4):
    for col in range(4):
        button = Button(root, text=buttons[row][col],
                command=lambda row=row, col=col: click(buttons[row][col]))
        button.grid(row=row + 2, column=col, sticky="nsew")

root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(4, weight=1)

root.mainloop()