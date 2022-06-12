# 1) Сделать калькулятор с 4 действиями
# 2) Добавить комплексные числа
import cmath
from unicodedata import decimal


rawdata = input("\nВведите выражение для расчёта через пробел, например 25 + 17\n")

def calculate(rawdata):

    data = list(rawdata.split())
    print (f' Исходный список: {data}')
    

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
    return (f"{operand1} {operation} {operand2} = {result}")

print (calculate(rawdata))