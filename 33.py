# 33.	Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random

k = (int(input("Введите натуральную степень k = ")))

data = open('formula 33.txt', 'a') # a - добавить, w - перезаписать, r - чтение

for i in range (1,k+1):
    # случ коэффициент умножить на x в степени k плюс
    currentPower = k+1-i
    c = random.randint(0,100)
    data.write(f'{c}x^{currentPower}+')

data.write(f'{random.randint(0,100)}=0\n')

